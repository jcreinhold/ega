<!-- original page 182 -->

## §22. Differential criteria for formal smoothness and regularity

The principal results of this section are:

a) The criteria `(22.2.2)` and `(22.5.8)`, which give necessary and sufficient conditions for a complete Noetherian
local ring $A$ containing a field $k$ to be formally smooth over $k$. The criterion `(22.5.8)` is stated without
involving any differential notion, and completes $(0_{IV}, 19.6.6)$; the statement `(22.2.2)`, of a somewhat more
technical nature, allows one to give a classification, for $k$ fixed, of the local rings $A$ considered `(22.2.5)`: they
are determined by their dimension $n$ and their residue field $K$, subject only to the condition $n \geq
rg_{K}(\Upsilon_{K/k})$.

b) The theorem `(22.3.3)`, and the corollary `(22.7.6)` of Nagata's Jacobian criterion `(22.7.3)`, which give conditions
allowing one to assert that a localization of a complete Noetherian local ring $A$ containing a field $k$ is
geometrically regular over $A$; they will play an important role in the study of the "fine" properties of local rings
carried out in Chap. IV, §7. For the moment we possess no proof of `(22.7.6)` independent of Nagata's Jacobian
criterion.

c) Zariski's Jacobian criterion `(22.6.7)` and its variants, which are easy consequences of $(0_{IV}, 20.7.8)$.

### 22.1. Lifting of formal smoothness

**Theorem (22.1.1).**

<!-- label: 0_IV.22.1.1 -->

*Let $s : \Lambda \to A$, $u : A \to B$ be two ring homomorphisms, $\mathfrak{J}$ an ideal of $B$, $C$ the quotient ring
$B/\mathfrak{J}$. Suppose that $C$ is a $\Lambda$-algebra formally smooth for the discrete topology.*

*(i) Suppose the following conditions are satisfied:*

*α) $\mathfrak{J}/\mathfrak{J}^{2}$ is a projective $C$-module.*

*β) The canonical homomorphism $S^{\bullet}_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to gr^{\bullet}_{\mathfrak{J}}(B)$
$(0_{IV}, 19.5.2)$ is bijective.*

*γ) The characteristic homomorphism $\chi : \Upsilon_{C/A/\Lambda} \to \mathfrak{J}/\mathfrak{J}^{2}$ $(0_{IV},
20.6.20)$ is injective.*

*δ) The $C$-module $\Omega^{1}_{B/\Lambda} \otimes_{B} C$ is projective.*

*Then $B$, equipped with the $\mathfrak{J}$-preadic topology, is a $\Lambda$-algebra formally smooth.*

*(ii) Conversely, suppose that $B$ is a $\Lambda$-algebra formally smooth for the $\mathfrak{J}$-preadic topology, and
that $A$ is a $\Lambda$-algebra formally smooth for the discrete topology. Then the conditions α), β), γ), δ) of (i) are
satisfied.*

By virtue of the exact sequence $(0_{IV}, 20.6.22.1)$ (which is applicable, since $B/\mathfrak{J}^{2}$ is a
$\Lambda$-trivial extension of $C$ by $\mathfrak{J}/\mathfrak{J}^{2}$, $C$ being supposed to be a $\Lambda$-algebra
formally smooth $(0_{IV}, 19.4.4)$), the condition γ) is equivalent to $\Upsilon^{C}_{B/A/\Lambda} = 0$, or equivalently
to the following:

γ′) *The homomorphism $u_{B/A/\Lambda} \otimes 1_{C} : \Omega^{1}_{A/\Lambda} \otimes_{A} C \to \Omega^{1}_{B/\Lambda}
\otimes_{B} C$ is injective.*

(i) The conditions α) and β) entail that $B$ is a $\Lambda$-algebra formally smooth for the $\mathfrak{J}$-preadic
topology $(0_{IV}, 19.5.4)$. It therefore amounts to the same to say that $B$ is (for the $\mathfrak{J}$-preadic
topology) a $\Lambda$-algebra formally smooth, or a $\Lambda$-algebra formally smooth relative to $A$. To see that $B$
is a $\Lambda$-algebra formally smooth, it suffices, by virtue of $(0_{IV}, 20.7.2)$, to prove that the continuous
homomorphism of topological $B$-modules $u_{B/A/\Lambda} : \Omega^{1}_{A/\Lambda} \otimes_{A} B \to
\Omega^{1}_{B/\Lambda}$ is formally left-invertible. Now, since $B$ is a $\Lambda$-algebra formally smooth, the
topological $B$-module $\Omega^{1}_{B/\Lambda}$ is formally projective $(0_{IV}, 20.4.9)$ and its topology is deduced
from that of $B$ $(0_{IV}, 20.4.5)$. By virtue of $(0_{IV}, 19.1.9)$, it therefore suffices, for $u_{B/A/\Lambda}$ to be
formally left-invertible, that $u_{B/A/\Lambda} \otimes 1_{C}$ be left-invertible. But by virtue of γ′), this last map
is injective, so one has the exact sequence $(0_{IV}, 20.6.14.7)$

```text
  0 → Ω^1_{A/Λ} ⊗_A C → Ω^1_{B/Λ} ⊗_B C → Ω^1_{B/A} ⊗_B C → 0.
```

Finally, by virtue of δ), the $C$-module $\Omega^{1}_{B/\Lambda} \otimes_{B} C$ is projective, so the preceding exact
sequence is *split*, which completes the proof of (i).

(ii) If $B$ is a $\Lambda$-algebra formally smooth for the $\mathfrak{J}$-preadic topology, and $A$ is a
$\Lambda$-algebra formally smooth for the discrete topology, then $B$ is a $A$-algebra formally smooth for the
$\mathfrak{J}$-preadic topology $(0_{IV}, 19.3.5, (ii))$; the conditions α) and β) therefore result from $(0_{IV},
19.5.6)$. Moreover, $(0_{IV}, 20.7.2)$ shows that $u_{B/A/\Lambda}$ is formally left-invertible, hence $u_{B/A/\Lambda}
\otimes 1_{C}$ is left-invertible $(0_{IV}, 19.1.7)$, and *a fortiori* injective.

<!-- original page 184 -->

Finally, $\Omega^{1}_{B/\Lambda}$ is a formally projective $B$-module $(0_{IV}, 20.4.9)$, and consequently
$\Omega^{1}_{B/\Lambda} \otimes_{B} C$ is a projective $C$-module $(0_{IV}, 19.2.4)$.

**Corollary (22.1.2).**

<!-- label: 0_IV.22.1.2 -->

*Let $s : \Lambda \to A$, $u : A \to B$ be two ring homomorphisms, $\mathfrak{m}$ a maximal ideal of $B$, $K =
B/\mathfrak{m}$ the quotient field. Suppose that the $\Lambda$-algebras $A$ and $K$ are formally smooth for the discrete
topology. Then the following conditions are equivalent:*

*a) $B$ is a $\Lambda$-algebra formally smooth for the $\mathfrak{m}$-preadic topology.*

*b) The canonical homomorphism*

$$ (22.1.2.1) S^{\bullet}_{K}(\mathfrak{m}/\mathfrak{m}^{2}) \to gr^{\bullet}_{\mathfrak{m}}(B) $$

*is bijective, and the characteristic homomorphism*

$$ (22.1.2.2) \chi : \Upsilon_{K/A/\Lambda} \to \mathfrak{m}/\mathfrak{m}^{2} $$

*is injective.*

This follows immediately from `(22.1.1)`, the conditions α) and δ) being here trivially satisfied, since $K$ is a field.

**Remark (22.1.3).**

<!-- label: 0_IV.22.1.3 -->

*Suppose the hypotheses of `(22.1.2)` are satisfied and moreover suppose that $\mathfrak{m}/\mathfrak{m}^{2}$ is a
$K$-vector space of finite rank. Then, for $B$ to be a $\Lambda$-algebra formally smooth for the $\mathfrak{m}$-preadic
topology, it suffices that the following conditions be satisfied:*

*(22.1.3.1) Given a polynomial algebra $E = K[T_{1}, \cdots, T_{n}]$, the maximal ideal $\mathfrak{n}$ of $E$ generated
by the $T_{i}$ ($1 \leq i \leq n$), and an ideal $\mathfrak{b} \supset \mathfrak{n}^{k}$ of $E$, every
$\Lambda$-homomorphism $v : B \to E/\mathfrak{b}$ which, by passage to the quotients, gives the identity $K \to K$,
factors as $B \xrightarrow{w} E/\mathfrak{n}^{k} \to E/\mathfrak{b}$, where $w$ is a $\Lambda$-homomorphism.*

*(22.1.3.2) If $F$ is the trivial extension $D_{K}(K)$ ("algebra of dual numbers over $K$"), $\rho : \Lambda \to F$ a
ring homomorphism such that the composite $\Lambda \xrightarrow{\rho} F \to K$ is the canonical homomorphism, then every
$\Lambda$-homomorphism $v : B \to K$ which, by passage to the quotients, gives the identity $K \to K$, factors as $B
\xrightarrow{w} F \to K$, where $w$ is a $\Lambda$-homomorphism (for the $\Lambda$-algebra structure on $F$ defined by
$\rho$).*

Indeed, we have seen $(0_{IV}, 19.5.5)$ that condition `(22.1.3.1)` entails that the canonical homomorphism `(22.1.2.1)`
is bijective. By virtue of `(22.1.2)`, it then suffices to see that the canonical homomorphism $u_{B/A/\Lambda} \otimes
1_{K} : \Omega^{1}_{A/\Lambda} \otimes_{A} K \to \Omega^{1}_{B/\Lambda} \otimes_{B} K$ is injective, or equivalently
(since these are $K$-vector spaces) that for every $K$-vector space $L$, the canonical homomorphism
$\operatorname{Der}_{\Lambda}(B, L) \to \operatorname{Der}_{\Lambda}(A, L)$ is *surjective* (by virtue of $(0_{IV},
20.4.8)$); it is clear that for this it is necessary and sufficient that the canonical homomorphism
$\operatorname{Der}_{\Lambda}(B, K) \to \operatorname{Der}_{\Lambda}(A, K)$ be surjective, whence our assertion, by
virtue of $(0_{IV}, 20.1.5)$.

One notes that the two conditions `(22.1.3.1)` and `(22.1.3.2)` are entailed by the following:

*(22.1.3.3) For every local Artinian $\Lambda$-algebra $E$ with residue field equal to $K$, and every nilpotent ideal
$\mathfrak{r}$ of $E$, every $\Lambda$-homomorphism $B \to E/\mathfrak{r}$ which, by passage to the quotients, gives the
identity $K \to K$, factors as $B \xrightarrow{u} E \to E/\mathfrak{r}$, where $u$ is a $\Lambda$-homomorphism.*

<!-- original page 185 -->

This result generalizes as follows.

**Proposition (22.1.4).**

<!-- label: 0_IV.22.1.4 -->

*Let $\phi : A \to B$ be a local homomorphism of Noetherian local rings, $k$ (resp. $K$) the residue field of $A$ (resp.
$B$). For $B$ to be a $A$-algebra formally smooth (for the preadic topologies), it is necessary and sufficient that for
every local Artinian ring $C$ with residue field equal to $K$, every local homomorphism $A \to C$ (making $C$ a
topological $A$-algebra), and every nilpotent ideal $\mathfrak{J}$ of $C$, every local $A$-homomorphism $B \to
C/\mathfrak{J}$ such that the homomorphism $K \to K$ obtained by passage to the quotients is the identity, factors as $B
\xrightarrow{f} C \to C/\mathfrak{J}$, where $f$ is a local $A$-homomorphism.*

The condition being necessary by definition $(0_{IV}, 19.3.1)$, we show that it is sufficient. Since the
$A$-homomorphisms of $B$ into a discrete local `Â`-algebra arise by extension from local $A$-homomorphisms of $B$ into
this algebra, one may reduce to the case where $A$ and $B$ are complete, by virtue of $(0_{IV}, 19.3.6)$. When $A$ is a
field $k$, the proposition follows from `(22.1.3.3)`, where one takes the prime subfield of $k$ for $\Lambda$, and from
$(0_{IV}, 19.6.1)$. In the general case, set $B_{0} = B \otimes_{A} k = B/\mathfrak{m}B$ ($\mathfrak{m}$ maximal ideal
of $A$), which is complete. If `C_0` is a local Artinian $k$-algebra with residue field equal to $K$, $\mathfrak{J}_{0}$
a nilpotent ideal of `C_0`, every local $k$-homomorphism $g_{0} : B_{0} \to C_{0}/\mathfrak{J}_{0}$ giving the identity
on $K$ by passage to the quotients, gives by composition a local $A$-homomorphism

```text
  g : B → B_0 → C_0/𝔍_0
```

which by hypothesis therefore factors as $B \to C_{0} \to C_{0}/\mathfrak{J}_{0}$, where $f$ is a local
$A$-homomorphism; but since `C_0` is a $k$-algebra, $f$ factors as $B \to B_{0} \xrightarrow{f_{0}} C_{0}$, where
$f_{0}$ is a local $k$-homomorphism. We see therefore that the hypotheses of the statement are still satisfied when one
substitutes `B_0` and $k$ for $B$ and $A$ respectively; hence `B_0` is a $k$-algebra formally smooth according to what
we have just seen. Applying $(0_{IV}, 19.7.2)$ and $(0_{IV}, 19.7.1)$, we see that there exists a complete Noetherian
local ring $B'$, a local homomorphism $A \to B'$ making $B'$ a flat $A$-module and a $A$-algebra formally smooth, and an
$A$-isomorphism $u_{0} : B_{0} \xrightarrow{\sim} B' \otimes_{A} k = B'_{0}$. Let $v_{0}$ be the inverse isomorphism of
$u_{0}$; we propose to show that there exists a local $A$-homomorphism $v : B \to B'$ such that $v_{0}$ arises from $v$
by passage to the quotients. For this, denote by $\mathfrak{n}$ and $\mathfrak{n}'$ the respective maximal ideals of $B$
and $B'$, and, for each $j$, let $w_{j} : B/(\mathfrak{n}^{j+1} + \mathfrak{m}B) \to B'/(\mathfrak{n}'^{j+1} +
\mathfrak{m}B')$ be the homomorphism deduced from $v_{0}$ by passage to the quotients; it will suffice to form for each
$j$ a local $A$-homomorphism $v_{j} : B/\mathfrak{n}^{j+1} \to B'/\mathfrak{n}'^{j+1}$ such that the diagrams

```text
  B/𝔫^{j+1} ──v_j──▸ B′/𝔫′^{j+1}              B/𝔫^{j+1} ────v_j────▸ B′/𝔫′^{j+1}
       │                  │                          │                       │
       ▼                  ▼                          ▼                       ▼
  B/𝔫^j ──v_{j-1}──▸ B′/𝔫′^j         B/(𝔫^{j+1} + 𝔪B) ─w_j─▸ B′/(𝔫′^{j+1} + 𝔪B′)
```

be commutative; $B$ and $B'$ being complete, the homomorphism $v = \lim v_{j}$ will answer the question. Now, the
recursive formation of $v_{j}$ results from the hypothesis on $B$ and from the

<!-- original page 186 -->

same reasoning as in $(0_{IV}, 19.3.10.1)$, using the lemma $(0_{IV}, 19.3.10.2)$ and the fact that $\mathfrak{n}'^{j} +
(\mathfrak{n}'^{j+1} + \mathfrak{m}B') = \mathfrak{n}'^{j} + \mathfrak{m}B'$. It then follows from $(0_{IV}, 19.7.1.4)$
that $v$ is an $A$-isomorphism, for $B'$ is a flat $A$-module, and $B$ is complete for the $\mathfrak{m}$-preadic
topology, the ideals $\mathfrak{m}^{j} B$ being closed in $B$ for the $\mathfrak{n}$-adic topology $(0_{I}, 7.3.5)$.
Q.E.D.

### 22.2. Differential characterization of local algebras formally smooth over a field

(22.2.1) Let $k$ be a field, $P$ its prime subfield, $A$ a $k$-algebra which is a local ring, $\mathfrak{m}$ its maximal
ideal, $K = A/\mathfrak{m}$ its residue field. Since $K$ is separable over $P$, $K$ is a $P$-algebra formally smooth for
the discrete topology $(0_{IV}, 19.6.1)$, and consequently the $P$-extension $A/\mathfrak{m}^{2}$ of $K$ by
$\mathfrak{m}/\mathfrak{m}^{2}$ is $P$-trivial, and the characteristic homomorphism

$$ (22.2.1.1) \chi_{A/k} : \Upsilon_{K/k} \to \mathfrak{m}/\mathfrak{m}^{2} $$

is therefore defined $(0_{IV}, 20.6.23)$.

**Theorem (22.2.2).**

<!-- label: 0_IV.22.2.2 -->

*Under the conditions of `(22.2.1)`, for $A$ to be a $k$-algebra formally smooth for the $\mathfrak{m}$-preadic
topology, it is necessary and sufficient that the following conditions be satisfied:*

*(i) The canonical homomorphism $S^{\bullet}_{K}(\mathfrak{m}/\mathfrak{m}^{2}) \to gr^{\bullet}_{\mathfrak{m}}(A)$ is
bijective.*

*(ii) The characteristic homomorphism $\chi_{A/k} : \Upsilon_{K/k} \to \mathfrak{m}/\mathfrak{m}^{2}$ is injective.*

This is a particular case of `(22.1.2)`, where one replaces $\Lambda$ by $P$, $A$ by $k$, and $B$ by $A$; $K$ and $k$,
being separable over $P$, are indeed $P$-algebras formally smooth $(0_{IV}, 19.6.1)$.

**Remark (22.2.3).**

<!-- label: 0_IV.22.2.3 -->

*Condition (ii) of `(22.2.2)` may be replaced by any of the following:*

*a) The canonical homomorphism $\Omega^{1}_{k} \otimes_{k} K \to \Omega^{1}_{A} \otimes_{A} K$ is injective.*

*b) For every $n$, the canonical homomorphism $\Omega^{1}_{k} \otimes_{k} (A/\mathfrak{m}^{n+1}) \to \Omega^{1}_{A/k}
\otimes_{A} (A/\mathfrak{m}^{n+1})$ is left-invertible.*

*c) The canonical homomorphism $\Omega^{1}_{k} \hat{\otimes}_{k} A \to \hat{\Omega}^{1}_{A}$ is left-invertible.*

*d) $A$ is a $k$-algebra formally smooth (for the $\mathfrak{m}$-preadic topology) relative to the prime field.*

Indeed, we have already remarked in `(22.1.1)` that the injectivity of $\chi_{A/k}$ is equivalent to a), and that the
conjunction of a) and condition (i) of `(22.2.2)` is equivalent to that of d) and (i). Finally, we have also seen in
`(22.1.1)` that b) and d) are equivalent, and the equivalence of b) and c) results from $(0_{IV}, 19.1.8)$.

(22.2.4) The principal application of `(22.2.2)` concerns local Noetherian and complete $k$-algebras (case where
$\mathfrak{m}/\mathfrak{m}^{2}$ is a $K$-vector space of finite rank). More precisely, let $k$ be a field, $K$ an
extension of $k$, $V$ a $K$-vector space of

<!-- original page 187 -->

finite rank; we consider the triples $(A, \alpha, \beta)$, where $A$ is a complete Noetherian local $k$-algebra formally
smooth with maximal ideal $\mathfrak{m}$, $\alpha : A/\mathfrak{m} \xrightarrow{\sim} K$ an isomorphism of $k$-algebras,
$\beta : \mathfrak{m}/\mathfrak{m}^{2} \xrightarrow{\sim} V$ a di-isomorphism of vector spaces (for the isomorphism
$\alpha$). Given two such triples $(A, \alpha, \beta)$, $(A', \alpha', \beta')$, an *equivalence* of the first onto the
second is a $k$-isomorphism $u : A \xrightarrow{\sim} A'$ such that (if $\mathfrak{m}'$ is the maximal ideal of $A'$)
the diagrams

```text
       gr^0(u)                         gr^1(u)
  A/𝔪 ────────▸ A′/𝔪′             𝔪/𝔪² ────────▸ 𝔪′/𝔪′²
    │              │                  │                │
   α│              │α′               β│                │β′
    ▼              ▼                  ▼                ▼
    K ───1_K────▸ K                   V ────1_V────▸ V
```

are commutative. It is immediate that the equivalence classes of triples $(A, \alpha, \beta)$ form a set, which we
denote $FL(K/k, V)$. We now remark that to every triple $(A, \alpha, \beta)$ is associated the composite
$K$-homomorphism of vector spaces $\Upsilon_{K/k} \xrightarrow{\chi_{A/k}} \mathfrak{m}/\mathfrak{m}^{2}
\xrightarrow{\beta} V$ (where $\chi_{A/k}$ is regarded as a di-homomorphism relative to $\alpha^{-1}$); the preceding
definition proves (by $(0_{IV}, 20.6.22.2)$) that this $K$-homomorphism *depends only on the equivalence class* of $(A,
\alpha, \beta)$ in $FL(K/k, V)$; in other words one has defined a canonical map

```text
  (22.2.4.1)   FL(K/k, V) → Hom_K(Υ_{K/k}, V).
```

**Proposition (22.2.5).**

<!-- label: 0_IV.22.2.5 -->

*Let $k$ be a field, $K$ an extension of $k$, $V$ a $K$-vector space of finite rank. The canonical map `(22.2.4.1)` is a
bijection of $FL(K/k, V)$ onto the set of injective $K$-homomorphisms of $\Upsilon_{K/k}$ into $V$.*

(i) To show that `(22.2.4.1)` is injective, one must prove the following: let $A$, $A'$ be two complete Noetherian local
$k$-algebras formally smooth, $\mathfrak{m}$, $\mathfrak{m}'$ their respective maximal ideals, $\alpha : A/\mathfrak{m}
\xrightarrow{\sim} K$, $\alpha' : A'/\mathfrak{m}' \xrightarrow{\sim} K$ two $k$-isomorphisms; suppose given two
$k$-isomorphisms $v^{0} : A/\mathfrak{m} \xrightarrow{\sim} A'/\mathfrak{m}'$, $v^{1} : \mathfrak{m}/\mathfrak{m}^{2}
\xrightarrow{\sim} \mathfrak{m}'/\mathfrak{m}'^{2}$ such that the diagrams

```text
                    v^0                                       v^1
  (22.2.5.1)   A/𝔪 ────▸ A′/𝔪′                 𝔪/𝔪² ────▸ 𝔪′/𝔪′²
                ╲       ╱                          ↖             ↗
                 α     α′                        χ_A         χ_{A′}
                  ╲   ╱                              ╲         ╱
                    K                                  Υ_{K/k}
```

are commutative. It is required to prove that there exists a $k$-isomorphism $u : A \xrightarrow{\sim} A'$ such that
$gr^{0}(u) = v^{0}$ and $gr^{1}(u) = v^{1}$. Note first that since $K$ is a field, the canonical homomorphism $(0_{IV},
20.6.7.1)$ is bijective $(0_{IV}, 20.6.11)$, hence there already exists a $k$-isomorphism $v : A/\mathfrak{m}^{2}
\xrightarrow{\sim} A'/\mathfrak{m}'^{2}$ such that $gr^{0}(v) = v^{0}$ and $gr^{1}(v) = v^{1}$. Note next that since
$A'$ is metrisable and complete, and $A$ a $k$-algebra formally smooth, the composite homomorphism $A \to
A/\mathfrak{m}^{2} \xrightarrow{v} A'/\mathfrak{m}'^{2}$ factors as $A \xrightarrow{u} A' \to A'/\mathfrak{m}'^{2}$,
where $u$ is

<!-- original page 188 -->

a $k$-homomorphism $(0_{IV}, 19.3.11)$, and we therefore already have $gr^{0}(u) = v^{0}$ and $gr^{1}(u) = v^{1}$. Now,
one has the commutative diagram

```text
  S_K^•(𝔪/𝔪²)  ────────▸  gr_𝔪^•(A)
       │                         │
       │ w                       │ gr^•(u)
       ▼                         ▼
  S_K^•(𝔪′/𝔪′²) ───────▸  gr_{𝔪′}^•(A′)
```

where the horizontal arrows are the canonical homomorphisms, and $w$ arises from $v^{0}$ and $v^{1}$; since $v^{0}$ and
$v^{1}$ are bijective, the same holds for $w$, and since $A$ and $A'$ are $k$-algebras formally smooth, one deduces from
`(22.2.2, (i))` that $gr^{\bullet}(u)$ is bijective. But since $A$ and $A'$ are separated and complete, this entails
that $u$ itself is bijective (Bourbaki, *Alg. comm.*, chap. III, §2, n° 8, cor. 3 of th. 1).

(ii) It remains to show that the image of `(22.2.4.1)` is the set of *injective* homomorphisms of $\Upsilon_{K/k}$ into
$V$; we already know by `(22.2.2, (ii))` that it is contained in this set; it will then suffice to prove the

**Lemma (22.2.5.2).**

<!-- label: 0_IV.22.2.5.2 -->

*For every $K$-homomorphism $h : \Upsilon_{K/k} \to V$, there exists a $k$-algebra $A$ which is a complete regular
Noetherian local ring, with maximal ideal $\mathfrak{m}$, residue field $K$, and a $K$-isomorphism $\beta :
\mathfrak{m}/\mathfrak{m}^{2} \xrightarrow{\sim} V$ such that $h = \beta \circ \chi_{A/k}$.*

Indeed, if this lemma is proved, the fact that $A$ is regular entails that condition (i) of `(22.2.2)` is satisfied
$(0_{IV}, 17.1.1)$; if moreover $h$ is injective, `(22.2.2)` will show that $A$ is a $k$-algebra formally smooth whose
class will have $h$ for image (on the other hand, if $h$ is not injective, the $k$-algebra $A$ whose existence
`(22.2.5.2)` proves is not formally smooth).

To prove `(22.2.5.2)`, let $B$ be the $K$-algebra $S^{\bullet}_{K}(V)$, $\mathfrak{n}$ the augmentation ideal of $B$,
and $A = \hat{B}$ the completed $K$-algebra of $B$ for the $\mathfrak{n}$-preadic topology (so that $A$ is isomorphic to
the algebra of formal series $K[[T_{1}, \cdots, T_{n}]]$ if $n = rg_{K}(V)$). By virtue of $(0_{IV}, 20.6.11)$ there
exists on $A/\mathfrak{m}^{2}$ (where $\mathfrak{m} = \mathfrak{n} A$) a structure of $k$-extension of $K$ by $V$
(distinct in general from the $k$-trivial structure defined by the canonical injection $k \to K \to A$) such that $h$ is
the characteristic homomorphism of this extension. If $f : k \to A/\mathfrak{m}^{2}$ is the structural homomorphism, the
fact that $k$ is separable over the prime field permits $(0_{IV}, 19.6.1)$ factoring $f$ as $k \xrightarrow{g} A \to
A/\mathfrak{m}^{2}$, and the $k$-algebra $A$ so defined answers the question $(0_{IV}, 20.6.22.2)$.

**Theorem (22.2.6).**

<!-- label: 0_IV.22.2.6 -->

*Let $k$ be a field, $K$ an extension of $k$. For there to exist a Noetherian local $k$-algebra $A$, with maximal ideal
$\mathfrak{m}$, such that $A/\mathfrak{m} = K$ and $A$ is formally smooth (for its $\mathfrak{m}$-preadic topology), it
is necessary and sufficient that $\Upsilon_{K/k}$ be a $K$-vector space of finite rank. The $k$-algebra $A$ is then
determined (up to a $k$-isomorphism giving by passage to the quotients the identity $K \to K$) by its dimension, which
is subject only to the condition $\geq rg_{K}(\Upsilon_{K/k})$.*

Since $\mathfrak{m}/\mathfrak{m}^{2}$ is of finite rank over $K$, the necessity of the condition follows from
`(22.2.2, (ii))`; conversely, `(22.2.5)` shows that the condition is sufficient and that one may take for
$\mathfrak{m}/\mathfrak{m}^{2}$ a $K$-vector space of arbitrary rank $\geq rg_{K}(\Upsilon_{K/k})$.

<!-- original page 189 -->

In particular, the identity homomorphism of $\Upsilon_{K/k}$ canonically associates to $K$ a complete Noetherian
$k$-algebra, formally smooth, for which $\Upsilon_{K/k}$ is isomorphic to $\mathfrak{m}/\mathfrak{m}^{2}$.

**Remarks (22.2.7).**

<!-- label: 0_IV.22.2.7 -->

*(i) Let $\Lambda$ be a Noetherian local ring with residue field $k$; it follows from $(0_{IV}, 19.7.1)$ and $(0_{IV},
19.7.2)$ that the determination of the $\Lambda$-algebras $A$ which are complete Noetherian local rings and which are
formally smooth is equivalent to the same problem where $\Lambda$ is replaced by $k$, and is thus in principle entirely
resolved by `(22.2.5)`, which reduces the question to the structure of the residue fields of the sought-for
$k$-algebras, as extensions of $k$.*

*(ii) The fact that $\Upsilon_{K/k}$ is of finite rank over $K$ does not entail that $K$ is "of finite radicial
multiplicity" over $k$ (cf. $(0_{IV}, 19.6.6)$). For example, let $k_{0}$ be a perfect field of characteristic $p > 0$,
$k = k_{0}(T)$ the field of rational fractions in one indeterminate over $k_{0}$, and $K = k^{p^{-\infty}}$ the smallest
perfect extension of $k$. One then has $\Omega^{1}_{k} = \Omega^{1}_{k/k_{0}} = 0$ $(0_{IV}, 21.4.4)$, hence by
definition $(0_{IV}, 20.6.1.1)$ $\Upsilon_{K/k} = \Omega^{1}_{K} \otimes_{k} K$, and since $k^{p} = k_{0}(T^{p})$, $T$
is a $p$-basis of $k$ over $k^{p}$, hence $(0_{IV}, 21.4.5)$, $\Omega^{1}_{K}$ is of rank `1` over $k$, and consequently
$\Upsilon_{K/k}$ of rank `1` over $K$. But for every $n$ the residue field of the local ring $K \otimes_{k} k^{p^{-n}}$
is isomorphic to $K$ and is therefore not separable over $k^{p^{-n}}$.*

The theorem `(22.2.2)` generalizes as follows.

**Proposition (22.2.8).**

<!-- label: 0_IV.22.2.8 -->

*Under the conditions of `(22.2.1)`, suppose that the characteristic $p$ of $k$ is `> 0`; let $(k_{\alpha})$ be a
decreasing filtered family of subfields of $k$, such that $\bigcap_{\alpha} k_{\alpha}(k^{p}) = k^{p}$. Then condition
(ii) of `(22.2.2)` can be replaced by any of the following:*

*a) There exists $\alpha_{0}$ such that the canonical homomorphism*

```text
  Ω^1_{k/k_α} ⊗_k K → Ω^1_{A/k_α} ⊗_A K
```

*is injective for every $\alpha \geq \alpha_{0}$.*

*b) There exists $\alpha_{0}$ such that $A$ is a $k$-algebra formally smooth (for the $\mathfrak{m}$-preadic topology)
relative to $k_{\alpha}$, for every $\alpha \geq \alpha_{0}$.*

*c) For every $\alpha$ and every integer $n \geq 0$, the canonical homomorphism*

```text
  Ω^1_{k/k_α} ⊗_k (A/𝔪^{n+1}) → Ω^1_{A/k_α} ⊗_A (A/𝔪^{n+1})
```

*is left-invertible.*

Indeed, if $A$ is a $k$-algebra formally smooth, it is so *a fortiori* relative to any subfield of $k$, which entails c)
by virtue of $(0_{IV}, 20.7.2)$ and $(0_{IV}, 19.1.7)$; it is clear that c) implies b), by virtue of $(0_{IV}, 20.7.2)$,
and that b) implies a). Finally, taking account of `(22.2.3)`, it remains to prove that a) entails that the canonical
homomorphism $u : \Omega^{1}_{k} \otimes_{k} K \to \Omega^{1}_{A} \otimes_{A} K$ is *injective*. Now, for every $\alpha$
one has a commutative diagram

```text
  Ω^1_k ⊗_k K ──────u──────▸ Ω^1_A ⊗_A K
       │                            │
       │ v_α                        │
       ▼                            ▼
  Ω^1_{k/k_α} ⊗_k K ──u_α──▸ Ω^1_{A/k_α} ⊗_A K
```

<!-- original page 190 -->

and the hypothesis that $u_{\alpha}$ is injective for $\alpha \geq \alpha_{0}$ implies that $Ker(u)$ is contained in the
intersection of the $Ker(v_{\alpha})$. But we have seen $(0_{IV}, 21.8.3)$ that this intersection is zero by virtue of
the hypothesis $\bigcap_{\alpha} k_{\alpha}(k^{p}) = k^{p}$, which completes the proof.

**Proposition (22.2.9).**

<!-- label: 0_IV.22.2.9 -->

*Under the hypotheses of `(22.2.1)`, the following conditions are equivalent:*

*a) $A/\mathfrak{m}^{2}$ is a $k$-trivial $k$-extension of $K$ by $\mathfrak{m}/\mathfrak{m}^{2}$.*

*b) $\chi_{A/k} = 0$.*

*c) The canonical homomorphism (0_IV, 20.5.11.2)*

```text
  δ_{K/A/k} : 𝔪/𝔪² → Ω^1_A ⊗_A K
```

*is injective (in other words, the sequence*

```text
  (22.2.9.1)   0 → 𝔪/𝔪² → Ω^1_A ⊗_A K → Ω^1_K → 0
```

*is exact).*

The equivalence of b) and c) results from the exact sequence $(0_{IV}, 20.6.22.1)$; the equivalence of c) and a) results
from $(0_{IV}, 20.5.12)$, the sequence `(22.2.9.1)` being split if it is exact, since these are vector spaces.

One notes that if $K$ is separable over $k$, the equivalent conditions of `(22.2.9)` are satisfied, by virtue of the
definition of $\chi_{A/k}$ `(22.2.1)` and of $(0_{IV}, 20.6.3)$.

**Corollary (22.2.10).**

<!-- label: 0_IV.22.2.10 -->

*Under the hypotheses of `(22.2.1)`, consider a subfield $k_{0}$ of $k$. The following conditions are equivalent:*

*a) $A/\mathfrak{m}^{2}$ is a $k_{0}$-trivial $k$-extension of $K$ by $\mathfrak{m}/\mathfrak{m}^{2}$.*

*b) The composite homomorphism $\Upsilon_{K/k_{0}} \to \Upsilon_{K/k} \xrightarrow{\chi_{A/k}}
\mathfrak{m}/\mathfrak{m}^{2}$ is zero.*

*c) The characteristic homomorphism $\chi_{A/k} : \Upsilon_{K/k} \to \mathfrak{m}/\mathfrak{m}^{2}$ factors as
$\Upsilon_{K/k} \to \Upsilon_{K/k/k_{0}} \xrightarrow{\chi'} \mathfrak{m}/\mathfrak{m}^{2}$.*

*Moreover, when these conditions are fulfilled, the homomorphism $\chi'$ is uniquely determined and coincides with the
characteristic homomorphism of the $k_{0}$-trivial $k$-extension $A/\mathfrak{m}^{2}$ of $K$ by
$\mathfrak{m}/\mathfrak{m}^{2}$.*

Since the composite in b) is none other than $\chi_{A/k_{0}}$, the equivalence of a) and b) results from `(22.2.9)`; on
the other hand, b) and c) are equivalent by virtue of the exact sequence $(0_{IV}, 20.6.18.1)$

$$ \Upsilon_{K/k_{0}} \to \Upsilon_{K/k} \to \Upsilon_{K/k/k_{0}} \to 0 $$

and since the canonical homomorphism $\Upsilon_{K/k} \to \Upsilon_{K/k/k_{0}}$ is surjective, this implies the
uniqueness of $\chi'$; the fact that $\chi'$ is the characteristic homomorphism of the $k_{0}$-extension
$A/\mathfrak{m}^{2}$ results from $(0_{IV}, 20.6.22.2)$.

**Corollary (22.2.11).**

<!-- label: 0_IV.22.2.11 -->

*Under the hypotheses of `(22.2.1)`, let $p$ be the characteristic exponent of $k$, and let $(k_{\alpha})$ be a
decreasing filtered family of subfields of $k$ such that $\bigcap_{\alpha} k_{\alpha}(k^{p}) = k^{p}$. If
$\Upsilon_{K/k}$ is of finite rank over $K$, there exists an index $\alpha$ such that $A/\mathfrak{m}^{2}$ is a
$k_{\alpha}$-trivial $k$-extension of $K$ by $\mathfrak{m}/\mathfrak{m}^{2}$.*

We know $(0_{IV}, 21.8.3)$ that there exists then an index $\alpha$ such that the canonical homomorphism $\Upsilon_{K/k}
\to \Upsilon_{K/k/k_{\alpha}}$ is bijective, hence condition b) of `(22.2.10)` (where $k_{\alpha}$ replaces $k_{0}$) is
satisfied.

<!-- original page 191 -->

### 22.3. Application to the relations between certain local rings and their completions

**Lemma (22.3.1).**

<!-- label: 0_IV.22.3.1 -->

*Let `A_0` be a Noetherian semi-local ring, $A$ a finite `A_0`-algebra (which is thus a Noetherian semi-local ring, cf.
Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9). If $\hat{A}_{0}$ and `Â` are the completions of `A_0`
and $A$ for their respective preadic topologies, then, when one equips `A_0`, $A$ and `Â` with the discrete topologies,
`Â` is a $A$-algebra formally smooth relative to `A_0` $(0_{IV}, 19.9.1)$.*

We know indeed that $\hat{A} = A \otimes_{A_{0}} \hat{A}_{0}$ (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of
prop. 9 and chap. III, §3, n° 4, th. 1), so the proposition results from $(0_{IV}, 19.9.3)$.

**Proposition (22.3.2).**

<!-- label: 0_IV.22.3.2 -->

*Let $A$ be a regular Noetherian local ring, $K$ its field of fractions, $p$ the characteristic of $K$. Suppose one of
the following hypotheses is satisfied:*

*(i) $p = 0$.*

*(ii) $p > 0$ and there exists a decreasing filtered family $(A_{\alpha})$ of Noetherian subrings of $A$, such that $A$
is a finite $A_{\alpha}$-algebra for every $\alpha$, that $A^{p^{h(\alpha)}} \subset A_{\alpha}$ for a suitable integer
$h(\alpha)$, and that, if $K_{\alpha}$ denotes the field of fractions of $A_{\alpha}$, one has $\bigcap_{\alpha}
K_{\alpha}(K^{p}) = K^{p}$.*

*Let then $B$ be an integral finite $A$-algebra containing $A$, $\mathfrak{n}$ a prime ideal of $B$, $C$ the local ring
$B_{\mathfrak{n}}$, $\mathfrak{q}$ a prime ideal of the completion `Ĉ` such that $\mathfrak{q} \cap C = 0$, so that the
local ring $\hat{C}_{\mathfrak{q}}$ is an algebra over the field of fractions $L$ of $B$. Then $\hat{C}_{\mathfrak{q}}$
is an $L$-algebra formally smooth for its $\mathfrak{q}$-adic topology, and consequently a geometrically regular ring
over $L$ $(0_{IV}, 19.6.5)$.*

Let us distinguish two cases.

I) Suppose that $\mathfrak{n}$ contains the maximal ideal $\mathfrak{m}$ of $A$, and consequently $\mathfrak{n} \cap A =
\mathfrak{m}$. Then $\mathfrak{n}$ is maximal (Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, prop. 1) and if $\mathfrak{r}$
is the radical of the semi-local ring $B$, `Ĉ` is the separated completion of $B$ for the $\mathfrak{n}$-preadic
topology, and one of the components of the semi-local ring $\hat{B}$, the completion of $B$ for the
$\mathfrak{r}$-preadic topology (Bourbaki, *Alg. comm.*, chap. III, §3, n° 4, prop. 8); one may therefore write
$\hat{C}_{\mathfrak{q}} = \hat{B}_{\mathfrak{q}'}$, where $\mathfrak{q}'$ is the prime ideal of $\hat{B}$ inverse image
of $\mathfrak{q}$. Note now that $B$ is a subring of $\hat{B}$ and the hypothesis $\mathfrak{q} \cap C = 0$ entails
$\mathfrak{q}' \cap B = 0$, hence $\hat{B}_{\mathfrak{q}'}$ is also the localization of the ring $\hat{B} \otimes_{B} L$
at one of its prime ideals $\mathfrak{q}''$, of which $\mathfrak{q}'$ is the inverse image in $\hat{B}$. Moreover one
has $\hat{B} = \hat{A} \otimes_{A} B$ (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. of prop. 9 and chap. III, §3, n°
4, th. 1), hence $\hat{B} \otimes_{B} L = \hat{A} \otimes_{A} L$; finally, if $\mathfrak{p}$ is the prime ideal of `Â`,
inverse image of $\mathfrak{q}''$, the fact that $A \to B$ is injective and the commutativity of the diagram

```text
  B ────▸ B̂
  ▲       ▲
  │       │
  A ────▸ Â
```

entail that $\mathfrak{p} \cap A = 0$, hence $(\hat{A} \otimes_{A} L)_{\mathfrak{q}''}$ is also localized of the ring

```text
  Â ⊗_A L = (Â ⊗_A K) ⊗_K L
```

<!-- original page 192 -->

at one of its prime ideals. To show that this local ring is an $L$-algebra formally smooth, it therefore suffices to
prove that $\hat{A}_{\mathfrak{p}} \otimes_{A} K$ is a $K$-algebra formally smooth $(0_{IV}, 19.3.5, (iii) and (iv))$;
moreover $\hat{A}_{\mathfrak{p}} \otimes_{A} K = \hat{A}_{\mathfrak{p}}$ since $\mathfrak{p} \cap A = 0$. We are going
to apply the criteria `(22.2.2)` and `(22.2.8)`. In the first place, since $A$ is regular, so is `Â` $(0_{IV}, 17.1.5)$,
hence so is $\hat{A}_{\mathfrak{p}}$ $(0_{IV}, 17.3.2)$, and condition (i) of `(22.2.2)` is satisfied $(0_{IV},
17.1.1)$. It therefore suffices (when $p > 0$) to verify condition b) of `(22.2.8)`. Now, `(22.3.1)` shows that, for
every $\alpha$, `Â` is an $A$-algebra formally smooth relative to $A_{\alpha}$ (for the discrete topologies);
consequently $\hat{A} \otimes_{A_{\alpha}} K_{\alpha} = \hat{A} \otimes_{A} (A \otimes_{A_{\alpha}} K_{\alpha})$ is a
$(A \otimes_{A_{\alpha}} K_{\alpha})$-algebra formally smooth relative to $K_{\alpha}$, for the discrete topologies
$(0_{IV}, 19.9.2, (iii))$. But since $A$ is a finite $A_{\alpha}$-algebra, one has $A \otimes_{A_{\alpha}} K_{\alpha} =
K$; since $\hat{A}_{\mathfrak{p}}$ is a localization of $\hat{A} \otimes_{A} K$, one concludes $(0_{IV}, 19.9.2, (iv))$
that $\hat{A}_{\mathfrak{p}}$ is a $K$-algebra formally smooth relative to $K_{\alpha}$, for the discrete topology, and
*a fortiori* for its $\mathfrak{p}$-adic topology ($(0_{IV}, 19.3.8)$ and $(0_{IV}, 19.9.5)$). But this is precisely
condition b) of `(22.2.8)`, hence the proposition is proved in this case for $p > 0$. When $p = 0$, the residue field of
$\hat{A}_{\mathfrak{p}}$ is separable over $K$, and since $\hat{A}_{\mathfrak{p}}$ is a regular ring, it is a
$K$-algebra formally smooth by virtue of $(0_{IV}, 19.6.4)$.

II) General case. Let $\mathfrak{s}$ be the prime ideal $\mathfrak{n} \cap A$ of $A$, and set $S = A - \mathfrak{s}$, so
that $S^{-1} A = A_{\mathfrak{s}}$, and one has $C = (S^{-1} B)_{S^{-1} \mathfrak{n}}$, where this time $S^{-1}
\mathfrak{n}$ contains the maximal ideal $\mathfrak{s} A_{\mathfrak{s}}$ of $A_{\mathfrak{s}}$. Since $A_{\mathfrak{s}}$
is regular $(0_{IV}, 17.3.2)$ and $S^{-1} B$ is an integral finite $A_{\mathfrak{s}}$-algebra containing
$A_{\mathfrak{s}}$, all reduces to verifying condition (ii) for $A_{\mathfrak{s}}$ when $p > 0$: now, set
$\mathfrak{s}_{\alpha} = \mathfrak{s} \cap A_{\alpha}$ and consider the local ring
$(A_{\alpha})_{\mathfrak{s}_{\alpha}}$. For every $t \notin \mathfrak{s}$, we have by hypothesis, on setting $q =
p^{h(\alpha)}$, $t^{q} \in A_{\alpha}$ and $t \notin \mathfrak{s}$, hence $t^{q} \notin \mathfrak{s}_{\alpha}$; if one
sets $S_{\alpha} = A_{\alpha} - \mathfrak{s}_{\alpha}$, one sees that one has $A_{\mathfrak{s}} = S^{-1}_{\alpha} A$,
and the hypothesis entails that $A_{\mathfrak{s}}$ is a finite $(A_{\alpha})_{\mathfrak{s}_{\alpha}}$-algebra; moreover,
$K_{\alpha}$ is also the field of fractions of $(A_{\alpha})_{\mathfrak{s}_{\alpha}}$, which completes the proof.

**Theorem (22.3.3).**

<!-- label: 0_IV.22.3.3 -->

*Let $A$ be a complete Noetherian local ring, $\mathfrak{p}$ a prime ideal of $A$, $B$ the localized ring
$A_{\mathfrak{p}}$, $\mathfrak{q}$ a prime ideal of the completion $\hat{B}$, $\mathfrak{r} = \mathfrak{q} \cap B$. Then
the localized ring $\hat{B}_{\mathfrak{q}}$ of $\hat{B}$ is a $B_{\mathfrak{r}}$-algebra formally smooth for the preadic
topologies.*

The prime ideal $\mathfrak{r}$ of $B$ is of the form $\mathfrak{n}_{\mathfrak{p}}$, where $\mathfrak{n} \subset
\mathfrak{p}$ is a prime ideal of $A$, and one has $B_{\mathfrak{r}} = A_{\mathfrak{n}}$; let $k$ be the residue field
of $B_{\mathfrak{r}}$, which is also the field of fractions of the complete integral local ring $A' = A/\mathfrak{n}$.
Since $\hat{B}$ is a flat $B$-module $(0_{I}, 7.3.5)$, $\hat{B}_{\mathfrak{q}}$ is a flat $B_{\mathfrak{r}}$-module
$(0_{I}, 6.3.2)$, and to prove that $\hat{B}_{\mathfrak{q}}$ is a $B_{\mathfrak{r}}$-algebra formally smooth, it
suffices to prove that $\hat{B}_{\mathfrak{q}} \otimes_{B} k = \hat{B}_{\mathfrak{q}}/\mathfrak{r}
\hat{B}_{\mathfrak{q}}$ is a $k$-algebra formally smooth $(0_{IV}, 19.7.1)$. Now $\hat{B}_{\mathfrak{q}}/\mathfrak{r}
\hat{B}_{\mathfrak{q}} = (\hat{B}/\mathfrak{r} \hat{B})_{\mathfrak{q}'}$, where $\mathfrak{q}'$ is the canonical image
of $\mathfrak{q}$ in $\hat{B}/\mathfrak{r} \hat{B}$; one has by definition $\mathfrak{q}' \cap (B/\mathfrak{r}) = 0$ and
$B/\mathfrak{r} = A_{\mathfrak{p}'}$, where $\mathfrak{p}' = \mathfrak{p}/\mathfrak{n}$; moreover $\hat{B}/\mathfrak{r}
\hat{B}$ is the completion of $B/\mathfrak{r}$.

We are therefore reduced to proving the following corollary.

**Corollary (22.3.4).**

<!-- label: 0_IV.22.3.4 -->

*Let $A$ be a complete integral Noetherian local ring, $K$ its field of fractions, $\mathfrak{p}$ a prime ideal of $A$,
$B$ the localized ring $A_{\mathfrak{p}}$. Then, for every prime ideal $\mathfrak{q}$*

<!-- original page 193 -->

*of the completion $\hat{B}$, such that $\mathfrak{q} \cap B = 0$, the local ring $\hat{B}_{\mathfrak{q}}$ is a
$K$-algebra formally smooth for its $\mathfrak{q}$-adic topology, hence a geometrically regular ring over $K$.*

Indeed, it follows from $(0_{IV}, 19.8.9)$ that there exists a subring `A_0` of $A$ which is a ring of formal series
over a field of characteristic $p > 0$ or over a Cohen ring (recall that Cohen rings have a field of fractions of
characteristic `0`), and is such that $A$ is a finite `A_0`-algebra. Now, one knows that the ring `A_0` is regular
$(0_{IV}, 17.3.8)$ and verifies one of the hypotheses (i), (ii) of `(22.3.2)`, by virtue of $(0_{IV}, 21.8.8)$; it
suffices therefore to apply `(22.3.2)`, replacing $B$ by $A$ and $A$ by `A_0`.

### 22.4. Preliminary results on finite extensions of local rings whose maximal ideal has square zero

**Proposition (22.4.1).**

<!-- label: 0_IV.22.4.1 -->

*Let $A$ be a local ring whose maximal ideal $\mathfrak{m}$ has square zero, $K = A/\mathfrak{m}$ its residue field;
denote by $V$ the ideal $\mathfrak{m}$ regarded as a $K$-vector space. Let $T_{i}$ ($1 \leq i \leq r$) be
indeterminates, and for each $i$, let $F_{i}$ be a unitary polynomial of $A[T_{i}]$ of degree $d_{i}$; denote by $A'$
the quotient of the polynomial ring $A[T_{1}, \cdots, T_{r}]$ by the ideal $\mathfrak{b}$ generated by the $r$
polynomials $F_{i}$. Suppose that $A'$ is a local ring, and let $\mathfrak{m}'$ be its maximal ideal, $K' =
A'/\mathfrak{m}'$ its residue field. Then:*

*(i) If one sets $d = \prod^{r}_{i=1} d_{i}$, $A'$ is a free $A$-module of rank $d$, and one has $[K' : K] \leq d$.*

*(ii) For $[K' : K] = d$, it is necessary and sufficient that $A' \otimes_{A} K = A'/\mathfrak{m} A'$ be a field
(necessarily isomorphic to $K'$), in other words, that $\mathfrak{m}' = \mathfrak{m} A'$. One has in this case
$\mathfrak{m}'^{2} = 0$, and if $V'$ denotes the ideal $\mathfrak{m}'$ regarded as a $K'$-vector space, the canonical
homomorphism $V \otimes_{K} K' \to V'$ is bijective (and consequently $rg_{K'} V' = rg_{K} V$).*

Without supposing $A'$ local, it is evident, by Euclidean division and induction on $r$, that if $t_{i}$ is the class of
$T_{i}$ mod. $\mathfrak{b}$, the monomials $M_{\nu} = t^{\nu_{1}}_{1} \cdots t^{\nu_{r}}_{r}$, where $0 \leq \nu_{i}
\leq d_{i} - 1$, form a basis of the $A$-module $A'$. If $A'$ is supposed local, $K'$ is a quotient of $A'/\mathfrak{m}
A' = A' \otimes_{A} K$, hence $[K' : K] \leq [A' \otimes_{A} K : K] = d$, and there can be equality only if
$\mathfrak{m}' = \mathfrak{m} A'$, which proves (i) and the first assertion of (ii). On the other hand, it is clear that
when $\mathfrak{m}' = \mathfrak{m} A'$, one has $\mathfrak{m}'^{2} = 0$, and $V \otimes_{K} K' = \mathfrak{m}
\otimes_{A} A' = \mathfrak{m} A' = V'$ since $A'$ is a free $A$-module.

**Remark (22.4.2).**

<!-- label: 0_IV.22.4.2 -->

*When $A$ is Artinian (in other words $rg_{K}(V)$ finite), the hypothesis that $A'$ is local always entails that
$rg_{K'}(\mathfrak{m}'/\mathfrak{m}'^{2}) \geq rg_{K}(V)$, as we shall see later `(22.5.2)`. Note that these two ranks
can be equal without one having $\mathfrak{m}' = \mathfrak{m} A'$.*

**Proposition (22.4.3).**

<!-- label: 0_IV.22.4.3 -->

*The hypotheses on $A$ and the notations being those of `(22.4.1)`, suppose that the $F_{i}$ are of the form*

```text
  (22.4.3.1)   F_i(T_i) = T_i^{d_i} + ∑_{1 ≤ k ≤ d_i} c_{ik} T_i^{d_i − k}
```

*where $d_{i} \geq 2$ for every $i$, and $c_{ik} \in \mathfrak{m}$ ("Eisenstein polynomials"). Then:*

*(i) $A'$ is a local ring, and its residue field $K' = A'/\mathfrak{m}'$ is isomorphic to $K$.*

<!-- original page 194 -->

*(ii) The kernel of the canonical homomorphism $V \to V' = \mathfrak{m}'/\mathfrak{m}'^{2}$ is the ideal $\mathfrak{n}$
of $A$ generated by the $\xi_{i} = c_{i, d_{i}}$ ("constant terms" of the $F_{i}$), and the cokernel of this
homomorphism has for basis over $K'$ the images of the $T_{i}$; in particular, one has*

```text
  (22.4.3.2)   rg_{K′}(V′) = rg_K(V) + r − r′
```

*where $r' = rg_{K}(\mathfrak{n})$. When $rg_{K}(V)$ is finite (in other words when $A$ is Artinian), for $rg_{K'}(V') =
rg_{K}(V)$, it is necessary and sufficient that the $\xi_{i}$ be linearly independent over $K$.*

(i) It is clear that $A' \otimes_{A} K = A'/\mathfrak{m} A'$ is isomorphic to $K[T_{1}, \cdots, T_{r}]/\mathfrak{b}'$,
where $\mathfrak{b}'$ is the ideal generated by the $r$ polynomials $T^{d_{i}}_{i}$; this is therefore a local ring of
residue field $K$, whose maximal ideal is generated by the classes of the $T_{i}$ mod. $\mathfrak{b}'$, whence (i).

(ii) Let $t_{i}$ ($1 \leq i \leq r$) be the class of $T_{i}$ mod. $\mathfrak{b}$; it follows from (i) that the maximal
ideal $\mathfrak{m}'$ of $A'$ is given by

```text
  𝔪′ = 𝔪 A′ + ∑_{i=1}^r t_i A′
```

whence, taking account of $\mathfrak{m}^{2} = 0$,

```text
  𝔪′² = ∑_{i,j} t_i t_j A′ + ∑_i t_i 𝔪 A′.
```

One concludes that $A'/\mathfrak{m}'^{2}$ is isomorphic to the ring $A[T_{1}, \cdots, T_{r}]/\mathfrak{c}$, where
$\mathfrak{c}$ is the ideal generated by the elements

```text
  F_i  (1 ≤ i ≤ r),   T_i T_j  (1 ≤ i ≤ r, 1 ≤ j ≤ r),   x T_i  (1 ≤ i ≤ r, x ∈ 𝔪).
```

Since $d_{i} \geq 2$ and the $T^{d_{i}}_{i}$ belong to $\mathfrak{c}$, the hypotheses made entail that $\mathfrak{c}$ is
also generated by the elements

```text
  ξ_i  (1 ≤ i ≤ r),   T_i T_j  (1 ≤ i ≤ r, 1 ≤ j ≤ r),   T_i x  (1 ≤ i ≤ r, x ∈ 𝔪).
```

Let $\mathfrak{c}_{1} = \sum_{i,j} T_{i} T_{j} A[T_{1}, \cdots, T_{r}]$, $\mathfrak{c}_{2} = \mathfrak{c}_{1} + \sum_{i}
\mathfrak{m} T_{i} A[T_{1}, \cdots, T_{r}]$, so that $\mathfrak{c} = \mathfrak{c}_{2} + \sum_{i} \xi_{i} A[T_{1},
\cdots, T_{r}]$. It is clear that $A[T_{1}, \cdots, T_{r}]/\mathfrak{c}_{1}$ is the direct sum of $A$ and the $A
t^{(1)}_{i}$, where $t^{(1)}_{i}$ is the class of $T_{i}$ mod. $\mathfrak{c}_{1}$. One deduces that $A[T_{1}, \cdots,
T_{r}]/\mathfrak{c}_{2}$ is the direct sum of $A$ and the $K t^{(2)}_{i}$, where $t^{(2)}_{i}$ is the class of $T_{i}$
mod. $\mathfrak{c}_{2}$. Finally $A[T_{1}, \cdots, T_{r}]/\mathfrak{c}$ is the direct sum of $A/\mathfrak{n}$ and the $K
t_{i}'$, where $t_{i}'$ is the class of $T_{i}$ mod. $\mathfrak{c}$, and $\mathfrak{n}$ is the ideal of $A$ generated by
the $\xi_{i}$; in the identification of $A'/\mathfrak{m}'^{2}$ with $A[T_{1}, \cdots, T_{r}]/\mathfrak{c}$, the image of
$V$ identifies with $\mathfrak{m}/\mathfrak{n}$, and what precedes therefore proves (ii).

**Proposition (22.4.4).**

<!-- label: 0_IV.22.4.4 -->

*The hypotheses on $A$ and the notations being those of `(22.4.1)`, suppose that $K$ is of characteristic $p > 0$ (hence
$p \cdot 1 \in \mathfrak{m}$ in $A$) and that the $F_{i}$ are of the form*

```text
  (22.4.4.1)   F_i(T_i) = T_i^p + p ∑_{k=1}^{p−1} c_{ik} T_i^{p−k} − f_i
```

*with $c_{ik} \in A$ and $f_{i} \in A$ for every $i$ and every $k$ such that $1 \leq k \leq p - 1$; moreover, if $a_{i}$
is the class of $f_{i}$ mod. $\mathfrak{m}$, suppose that the family $(a_{i})_{1 \leq i \leq r}$ is $p$-free over
$K^{p}$ ("absolutely $p$-free"). Then:*

*(i) $A'$ is a local ring, of maximal ideal $\mathfrak{m} A'$, whose residue field $K'$ is isomorphic to the extension
of $K$ obtained by adjunction of the $a^{1/p}_{i}$ ($1 \leq i \leq r$).*

<!-- original page 195 -->

*(ii) The elements $d_{A} f_{i} \otimes 1_{K'}$ form a basis of the kernel $N = \Upsilon^{K'}_{A'/A}$ of the canonical
homomorphism $\Omega^{1}_{A} \otimes_{A} K' \to \Omega^{1}_{A'} \otimes_{A'} K'$.*

(i) This time $A' \otimes_{A} K = A'/\mathfrak{m} A'$ is isomorphic to $K[T_{1}, \cdots, T_{r}]/\mathfrak{b}'$, where
$\mathfrak{b}'$ is the ideal generated by the polynomials $T^{p}_{i} - a_{i}$; the hypothesis on the $a_{i}$ entails
that this quotient ring is a field $(0_{IV}, 21.1.8)$, whence the assertions of (i).

Before proving (ii), we establish the

**Lemma (22.4.4.2).**

<!-- label: 0_IV.22.4.4.2 -->

*Let $\Lambda$ be a ring, $A$ a $\Lambda$-algebra, $\mathfrak{J}$ an ideal of $A$ such that the ring $C =
A/\mathfrak{J}$ is of characteristic $p > 0$ (which is equivalent to saying that $p \cdot 1 \in \mathfrak{J}$ in $A$).
Let $\pi$ be the canonical image of $p \cdot 1$ in $\mathfrak{J}/\mathfrak{J}^{2}$. If $C$ is a $(\Lambda/p
\Lambda)$-algebra formally smooth for the discrete topologies, one has a canonical exact sequence*

```text
  (22.4.4.3)   0 → (𝔍/𝔍²)/C · π → Ω^1_{A/Λ} ⊗_A C → Ω^1_{C/Λ} → 0.
```

Set indeed $A' = A/p A$, $\mathfrak{J}' = \mathfrak{J}/p A$, so that $C = A'/\mathfrak{J}'$. Since $A' = A
\otimes_{\Lambda} (\Lambda/p \Lambda)$, one has $\Omega^{1}_{A/\Lambda} \otimes_{A} A' = \Omega^{1}_{A'/\Lambda'}$ up to
a canonical isomorphism, $\Lambda'$ denoting the ring $\Lambda/p \Lambda$ $(0_{IV}, 20.5.5)$. Applying then the exact
sequence $(0_{IV}, 20.5.14.1)$ to the $\Lambda'$-algebra $C = A'/\mathfrak{J}'$ formally smooth, one obtains the exact
sequence

```text
  0 → 𝔍′/𝔍′² → Ω^1_{A′/Λ′} ⊗_{A′} C → Ω^1_{C/Λ′} → 0
```

and since the homomorphism $\Lambda \to \Lambda'$ is surjective, one has $\Omega^{1}_{C/\Lambda'} =
\Omega^{1}_{C/\Lambda}$ up to a canonical isomorphism $(0_{IV}, 20.5.15)$; whence the exact sequence `(22.4.4.3)` by
virtue of what precedes.

(ii) Since one has $\mathfrak{m}^{2} = 0$, we shall again denote by $V'$ the ideal $\mathfrak{m}'$ regarded as a
$K'$-vector space, and we set

```text
  (22.4.4.4)   V_0 = V/K · p = 𝔪/(𝔪² + p A),   V′_0 = V′/K′ · p = 𝔪′/(𝔪′² + p A′).
```

Applying the exact sequence `(22.4.4.3)` to the case $\Lambda = \mathbb{Z}$, to the $\mathbb{Z}$-algebra $A$ (resp.
$A'$) and to its ideal $\mathfrak{m}$ (resp. $\mathfrak{m}'$), there arises, since $K$ (resp. $K'$) is separable over
the prime field $\mathbb{Z}/p \mathbb{Z}$, hence a $(\mathbb{Z}/p \mathbb{Z})$-algebra formally smooth $(0_{IV},
19.6.1)$, the exact sequences

```text
  (22.4.4.5)   0 → V_0 → Ω^1_A ⊗_A K → Ω^1_K → 0,    0 → V′_0 → Ω^1_{A′} ⊗_{A′} K′ → Ω^1_{K′} → 0.
```

Consider then the diagram `(22.4.4.6)` whose two middle columns are the second sequence `(22.4.4.5)` and the first
tensored by $K'$; since the first exact sequence `(22.4.4.5)` is formed of vector spaces over $K$, the two middle
columns of `(22.4.4.6)` are exact; moreover, the diagram formed by these columns and the horizontal arrows connecting
them is commutative, by virtue of the proof of `(22.4.4.2)` and of the commutativity of the diagram $(0_{IV},
20.5.11.3)$. The last line of `(22.4.4.6)` is the exact sequence obtained from $(0_{IV}, 20.6.1.1)$ by replacing $A$,
$B$, $C$ by $\mathbb{Z}$, $K$ and $K'$; the middle line is obtained by tensorisation with $K'$ of the exact sequence of
$K$-modules deduced from $(0_{IV}, 20.6.1.1)$ by replacing $A$, $B$, $C$ by $\mathbb{Z}$, $A$, $K$ respectively. The
diagram formed by these two lines and the vertical arrows connecting them is commutative by virtue of the commutativity
of $(0_{IV}, 20.6.4.3)$. Note on the other hand that one is under the conditions of application of `(22.4.1, (ii))`, so
the upper line of the diagram `(22.4.4.6)` is exact; the extreme columns of the diagram

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

Now, if $t_{i}$ is the canonical image of $T_{i}$ in $A'$, the relation $F_{i}(t_{i}) = 0$, together with the fact that
in $A'$ one has $p \cdot 1 \in \mathfrak{m} A' \subset \mathfrak{m}'$, shows at once that $d_{A'} f_{i} \in
\mathfrak{m}' \Omega^{1}_{A'}$, hence $d_{A'} f_{i} \otimes 1_{K'} = 0$; this proves that the $d_{A} f_{i} \otimes
1_{K'}$ belong to $N$. Moreover, their images in $\Upsilon_{K'/K}$ are the $d_{K} a_{i} \otimes 1_{K'}$, which form a
basis of $\Upsilon_{K'/K}$ over $K'$ $(0_{IV}, 21.4.7)$; taking account of `(22.4.4.7)`, this completes the proof of
`(22.4.4)`.

(22.4.5) Consider now two rings $A$, $B$ of characteristic $p > 0$, and two homomorphisms

```text
  A ─i→ B ─j→ A
```

<!-- original page 197 -->

verifying the conditions of $(0_{IV}, 21.3.1)$. Let furthermore $\mathfrak{m}$ be an ideal of square zero in $A$; set

```text
  K = A/𝔪,   B_{(K)} = B ⊗_A K = B/B i(𝔪)
```

and let

```text
  φ : A → K,   ψ : B → B_{(K)}
```

be the canonical homomorphisms.

Since $\phi$ is surjective, $\Omega^{1}_{B_{(K)}/A}$ identifies canonically with $\Omega^{1}_{B_{(K)}/K}$ $(0_{IV},
20.5.15)$. Note that, since $p \geq 2$, for every $x \in \mathfrak{m}$, one has $j(i(x)) = x^{p} = 0$, in other words
$j(i(\mathfrak{m})) = 0$; by passage to the quotients one therefore deduces from $j$ a homomorphism

$$ j' : B_{(K)} \to A $$

such that, if $i' = \psi \circ i : A \to B_{(K)}$, one has

```text
  j′(i′(x)) = x^p   and   i′(j′(y)) = y^p   for x ∈ A and y ∈ B_{(K)}.
```

On setting, following the notations of $(0_{IV}, 21.3.2)$,

```text
  Θ_{B_{(K)}/A} = Ω^1_{B_{(K)}/A} ⊗_{B_{(K)}} A_{[j′]} = Ω^1_{B_{(K)}/K} ⊗_{B_{(K)}} A_{[j′]},
```

one has $(0_{IV}, 21.3.2.2)$ a canonical homomorphism

$$ (22.4.5.1) \pi_{B_{(K)}/A} : \Theta_{B_{(K)}/A} \to \Omega^{1}_{A}. $$

On the other hand, one deduces from $i$ and $j$, by passage to the quotients (taking account of the fact that
$j(i(\mathfrak{m})) = 0$), homomorphisms

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

hence, on tensoring `(22.4.5.1)` with $K$, one obtains a canonical $K$-homomorphism

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

is commutative, $\pi_{B_{(K)}/K}$ being the canonical homomorphism corresponding to $i_{0}$ and $j_{0}$ $(0_{IV},
21.3.2.2)$. By restriction to $\Xi_{B_{(K)}/K} = Ker(\pi_{B_{(K)}/K})$, the homomorphism $\pi'_{B_{(K)}/K}$ therefore
defines a canonical homomorphism

```text
  (22.4.5.3)   Ξ_{B_{(K)}/K} → Ker(Ω^1_A ⊗_A K → Ω^1_K) = Υ_{K/A}.
```

(22.4.6) The hypotheses and notations being those of `(22.4.5)`, suppose moreover that $\mathfrak{m}$ is a maximal ideal
of square zero, hence $K$ a field, and denote by $V$ the ideal $\mathfrak{m}$ regarded as a $K$-vector space. Since $K$
is a formally smooth algebra over its prime field $\mathbb{F}_{p}$ $(0_{IV}, 21.5.2)$ and $A$ is an algebra over
$\mathbb{F}_{p}$ (so that $\Omega^{1}_{A} = \Omega^{1}_{A/\mathbb{F}_{p}}$), one deduces from $(0_{IV}, 20.5.14)$ that
one has an exact sequence

```text
  (22.4.6.1)   0 → V → Ω^1_A ⊗_A K → Ω^1_K → 0.
```

One has therefore by `(22.4.5.3)` a homomorphism denoted

$$ (22.4.6.2) \chi'_{B/A} : \Xi_{B_{(K)}/K} \to V $$

which we shall call the *characteristic homomorphism* of the $A$-algebra $B$ (relative to $i$, $j$ and $\mathfrak{m}$).
It results from the definitions that for $\chi'_{B/A}$ to be injective, it is necessary and sufficient that
$\pi'_{B_{(K)}/K}$ be injective, the kernel of the latter being evidently contained in $\Xi_{B_{(K)}/K}$.

**Proposition (22.4.7).**

<!-- label: 0_IV.22.4.7 -->

*Let $A$ be a local Artinian ring whose maximal ideal $\mathfrak{m}$ has square zero, $K = A/\mathfrak{m}$ its residue
field, $V$ the ideal $\mathfrak{m}$ regarded as a $K$-vector space; suppose that $A$ is of characteristic $p > 0$; let*

```text
  (22.4.7.1)   F_i(T_i) = T_i^p − f_i    with f_i ∈ A (1 ≤ i ≤ r)
```

*and denote by $B$ the quotient ring of $A[T_{1}, \cdots, T_{r}]$ by the ideal generated by the $r$ polynomials $F_{i}$.
Then:*

*(i) $B$ is a local ring.*

*(ii) If $\mathfrak{m}'$ is the maximal ideal of $B$, $K' = B/\mathfrak{m}'$ its residue field, $V'$ the $B$-module
$\mathfrak{m}'/\mathfrak{m}'^{2}$ regarded as a $K'$-vector space, then, for $rg_{K}(V) = rg_{K'}(V')$, it is necessary
and sufficient that the characteristic homomorphism of $K$-vector spaces*

$$ (22.4.7.2) \chi'_{B/A} : \Xi_{B_{(K)}/K} \to V $$

*(cf. `(22.4.6.2)`) be injective.*

Let us still denote by $a_{i}$ ($1 \leq i \leq r$) the class of $f_{i}$ mod. $\mathfrak{m}$; the $a_{i}$ are no longer
necessarily $p$-independent over $K^{p}$, but one may always suppose that the sub-family

<!-- original page 199 -->

$(a_{i})_{s+1 \leq i \leq r}$ is $p$-free over $K^{p}$ and forms a $p$-basis over $K^{p}$ of the field $K^{p}(a_{1},
\cdots, a_{r})$, so that one has

```text
  a_i ∈ K^p(a_{s+1}, …, a_r)   for 1 ≤ i ≤ s.
```

Denote by $A''$ the quotient ring of $A[T_{s+1}, \cdots, T_{r}]$ by the ideal generated by the $F_{i}$ of index $i \geq
s + 1$; then, by `(22.4.4)`, $A''$ is a local ring whose maximal ideal is $\mathfrak{m}'' = \mathfrak{m} A''$ (hence of
square zero) and the residue field $K'' = K(a^{1/p}_{s+1}, \cdots, a^{1/p}_{r})$. One therefore has $a_{i} \in K''^{p}$
for $1 \leq i \leq s$ and consequently, in $A''$, the element $f_{i}$, for $1 \leq i \leq s$, can be written

$$ (22.4.7.3) f_{i} = g^{p}_{i} + h_{i} $$

where $g_{i} \in A''$ and $h_{i} \in \mathfrak{m}''$ (since $\mathfrak{m}''^{2} = 0$ and $p \mathfrak{m}'' = 0$, it is
immediate that $h_{i}$ is determined uniquely by these conditions). Replacing $T_{i}$ by $T_{i} + g_{i}$, one sees
therefore that if one sets

```text
  G_i(T_i) = T_i^p + ∑_{k=1}^{p−1} (p choose k) g_i^{p−k} T_i^k − h_i    (1 ≤ i ≤ s)
```

$B$ is the quotient ring of $A''[T_{1}, \cdots, T_{s}]$ by the ideal generated by the $G_{i}$; now, all the coefficients
of $G_{i}$ except the leading coefficient belong to $\mathfrak{m}''$, hence one is in the situation of `(22.4.3)`, $B$
is a local ring, and its residue field $K'$ is isomorphic to $K''$, which proves (i) (which moreover follows directly
from $B^{p} \subset A$, and consequently there is only one ideal of $B$ over $\mathfrak{m}$).

Note now that for `(22.4.7.2)` to be injective, it is necessary and sufficient that the same hold for

```text
  π′_{B_{(K)}/K} : Ω^1_{B_{(K)}/B_{(K)}} K → Ω^1_A ⊗_A K
```

(by `(22.4.6)`). Now $B_{(K)} = B/\mathfrak{m} B$ is the quotient algebra of $C = K[T_{1}, \cdots, T_{r}]$ by the ideal
generated by the polynomials $\bar{F}_{i} = T^{p}_{i} - a_{i}$, and since $d_{C/K} \bar{F}_{i} = 0$ it follows from
$(0_{IV}, 20.5.13)$ that $\Omega^{1}_{B_{(K)}/K}$ is a free $B_{(K)}$-module having for basis the $d_{B_{(K)}/K} t_{i}$,
where $t_{i}$ is the canonical image of $T_{i}$ ($1 \leq i \leq r$). But by definition `(22.4.5)` the canonical image by
$j' : B_{(K)} \to A$ of a class mod. $\mathfrak{m} B$ of an element $x \in B$ is the element $x^{p} \in A$; one deduces
at once, since $t^{p}_{i} = f_{i}$, that the image of $d_{B_{(K)}/K} t_{i} \otimes 1$ by $\pi'_{B_{(K)}/K}$ is $d_{A}
f_{i} \otimes 1$ in $\Omega^{1}_{A} \otimes_{A} K$; the condition that $\pi'_{B_{(K)}/K}$ be injective is therefore
equivalent to the fact that the $d_{A} f_{i} \otimes 1_{K}$ are linearly independent over $K$, or equivalently that
their images $d_{A} f_{i} \otimes 1_{K'}$ are linearly independent over $K'$ in $\Omega^{1}_{A} \otimes_{A} K'$.

Now, if one applies `(22.4.4)` to the $A$-algebra $A''$, one sees that the kernel of the canonical homomorphism
$\Omega^{1}_{A} \otimes_{A} K' \to \Omega^{1}_{A''} \otimes_{A''} K'$ has for basis the $d_{A} f_{i} \otimes 1_{K'}$ for
$s + 1 \leq i \leq r$. The preceding condition therefore also amounts to saying that the $d_{A''} f_{i} \otimes 1_{K'}$
are linearly independent in $\Omega^{1}_{A''} \otimes_{A''} K'$ for $1 \leq i \leq s$. Now one has $d_{A''} f_{i} =
d_{A''} h_{i}$ by `(22.4.7.3)`; on the other hand, if $V''$ is the $K'$-vector space $\mathfrak{m}''$, one has
$rg_{K'}(V'') = rg_{K}(V)$ `(22.4.1, (ii))`, and the condition $rg_{K'}(V') = rg_{K}(V)$ is therefore equivalent to
$rg_{K'}(V') = rg_{K'}(V'')$. But it follows

<!-- original page 200 -->

from `(22.4.3)` that this last relation is equivalent to the fact that the classes $h_{i}$ in $V''$ are linearly
independent over $K'$. Now, in $\Omega^{1}_{A''} \otimes_{A''} K'$, the $d_{A''} h_{i} \otimes 1_{K'}$ are the canonical
images $(0_{IV}, 20.5.11.2)$ of the $h_{i}$ by the *injection* $V'' \to \Omega^{1}_{A''} \otimes_{A''} K'$ (cf.
`(22.4.6.1)`), and this completes proving `(22.4.7)`.

One has moreover proved:

**Corollary (22.4.7.4).**

<!-- label: 0_IV.22.4.7.4 -->

*For $rg_{K}(V) = rg_{K'}(V')$, it is necessary and sufficient that the elements $d_{A} f_{i} \otimes 1_{K}$ ($1 \leq i
\leq r$) be linearly independent in the $K$-vector space $\Omega^{1}_{A} \otimes_{A} K$.*

**Remark (22.4.8).**

<!-- label: 0_IV.22.4.8 -->

*One may define the homomorphisms `(22.4.5.2)` and `(22.4.6.2)` under slightly different conditions. Let $A$ be a ring,
$\mathfrak{m}$ an ideal of square zero in $A$, $K = A/\mathfrak{m}$, $p$ a prime number such that $p \cdot 1 \in
\mathfrak{m}$ (in other words $K$ is of characteristic $p$, but not necessarily $A$). Let on the other hand $B$ be an
$A$-algebra which is a faithfully flat $A$-module (so that $A \subset B$), and suppose one has*

```text
  (22.4.8.1)   y^p ∈ A + p B ⊂ A + 𝔪 B
```

*for every $y \in B$. If $y^{p} = x + p z$ with $x \in A$, $z \in B$, the class mod. $(A \cap p B)$ of $x$ is well
determined, and since $A \cap p B = p A$ (since $B$ is a faithfully flat $A$-module), one has thus defined a canonical
map $j : B \to A/p A$, such that, for $x \in A$, $j(x)$ is the class of $x^{p}$ mod. `p A`. Moreover, if $y' \in B$ and
$y'^{p} = x' + p z'$ with $x' \in A$, $z' \in B$, it is immediate that the elements $(y + y')^{p} - x - x'$ and $(y
y')^{p} - x x'$ belong to `p B` by virtue of the fact that the binomial coefficients `(p choose i)` are multiples of $p$
for $1 \leq i \leq p - 1$. The map $j$ is therefore a *ring homomorphism*. By composition, one deduces from $j$ a
homomorphism $j' : B \to A/p A \to A/\mathfrak{m} = K$ and consequently a homomorphism $j_{0} : B_{(K)} \to K$ such that
$j'$ is the composite $B \to B_{(K)} = B \otimes_{A} K \to K$; moreover, if $i_{0} : K \to B_{(K)}$ is the canonical
map, $i_{0}$ and $j_{0}$ verify the conditions of $(0_{IV}, 21.3.1)$ for the rings of characteristic $p$, $K$ and
$B_{(K)}$. This being so, to define a $K$-homomorphism $\pi'_{B_{(K)}/K} : \Omega^{1}_{B_{(K)}/K} \otimes_{B_{(K)}}
K_{[j_{0}]} \to \Omega^{1}_{A} \otimes_{A} K$, it suffices $(0_{IV}, 20.4.8)$ to define a $K$-derivation*

```text
  (22.4.8.2)   D_0 : B_{(K)} → Ω^1_A ⊗_A K
```

*where the second member is regarded as a $B_{(K)}$-module by means of $j_{0}$. For this, it suffices to define an
$A$-derivation*

```text
  (22.4.8.3)   D : B → Ω^1_A ⊗_A K
```

*which vanishes in $\mathfrak{m} B$ (the second member being regarded as $B$-module by means of $j'$). Now, if one has
the relation $y^{p} = x + p z$ with $y \in B$, $x \in A$, $z \in B$, the element $d_{A} x \otimes 1_{K}$ of
$\Omega^{1}_{A} \otimes_{A} K$ depends only on the class $j(y)$ mod. `p A` of $x$ (hence only on $y$), for every $t \in
A$ one has $d_{A}(p t) = p d_{A}(t)$, hence $d_{A}(p t) \otimes 1 = 0$ in $\Omega^{1}_{A} \otimes_{A} K = \Omega^{1}_{A}
/ \mathfrak{m} \Omega^{1}_{A}$, since $p \cdot 1 \in \mathfrak{m}$. One may therefore take*

```text
  D(y) = d_A x ⊗ 1_K.
```

*The fact that $D$ is a derivation results easily from the fact that $j$ is a ring homomorphism; moreover, for $t \in
A$, one has $d_{A}(t^{p} x) = t^{p} d_{A}(x) + p t^{p-1} x d_{A}(t)$ and one extracts from this that $D(t y) = t D(y)$,
hence $D$ is an $A$-derivation; finally, if one has moreover $t \in \mathfrak{m}$, one has*

<!-- original page 201 -->

*$D(t y) = t D(y) = 0$ since $\Omega^{1}_{A} \otimes_{A} K$ is annihilated by $\mathfrak{m}$. One has thus defined the
homomorphism `(22.4.5.2)` sought, and it is immediate to verify that the composite homomorphism*

```text
                          π_{B_{(K)}/K}
  Θ_{B_{(K)}/K} ─────────────────────────▸ Ω^1_A ⊗_A K → Ω^1_K
```

*is still the canonical homomorphism $\pi_{B_{(K)}/K}$ (relative to $i_{0}$ and $j_{0}$). One has therefore also a
canonical homomorphism analogous to `(22.4.5.3)`.*

*If now $K$ is a field, $A/p A$ is an $\mathbb{F}_{p}$-algebra, and one has the exact sequence (0_IV, 20.5.14)*

```text
  0 → V/p A → Ω^1_{A/p A} ⊗_{A/p A} K → Ω^1_K → 0
```

*and on the other hand one has the exact sequence (0_IV, 20.5.12.1)*

```text
  p A → Ω^1_A ⊗_A (A/p A) → Ω^1_{A/p A} → 0
```

*which shows, on tensoring with $K$, that the $K$-vector spaces $\Omega^{1}_{A} \otimes_{A} K$ and $\Omega^{1}_{A/p A}
\otimes_{A/p A} K$ are isomorphic. The analogue of `(22.4.6.2)` is therefore here a homomorphism*

```text
  (22.4.8.4)   Ξ_{B_{(K)}/K} → V/p A = 𝔪/(𝔪² + p A).
```

*This said, the criterion `(22.4.7)`, where one replaces $V$ and $V'$ by $V/p A$ and $V'/p B$ respectively, remains
valid supposing only that $K$ is of characteristic $p > 0$ (in other words, that $p \cdot 1 \in \mathfrak{m}$ in $A$),
and that the $F_{i}(T_{i})$ are of the more general form `(22.4.4.1)`: indeed, $B$ is a free $A$-module (hence
faithfully flat), and it suffices to take up again the reasoning of `(22.4.7)`, replacing therein `(22.4.6.2)` by
`(22.4.8.4)` and $V''$ by $V''/p A''$.*

### 22.5. Geometrically regular algebras and formally smooth algebras

**Proposition (22.5.1).**

<!-- label: 0_IV.22.5.1 -->

*Let $A$ be a regular local ring, $A'$ a local ring containing $A$ and which is a finite $A$-algebra, $\mathfrak{m}$
(resp. $\mathfrak{m}'$) the maximal ideal of $A$ (resp. $A'$), $K = A/\mathfrak{m}$ (resp. $K' = A'/\mathfrak{m}'$) its
residue field. For $A'$ to be a regular ring, it is necessary and sufficient that one have*

$$ (22.5.1.1) rg_{K}(\mathfrak{m}/\mathfrak{m}^{2}) = rg_{K'}(\mathfrak{m}'/\mathfrak{m}'^{2}). $$

Indeed, the first member of `(22.5.1.1)` is $\dim(A)$ $(0_{IV}, 17.1.1)$ and since $A \subset A'$ and $A'$ is a finite
$A$-algebra, $\dim(A') = \dim(A)$ $(0_{IV}, 16.1.5)$; the equality `(22.5.1.1)` is therefore necessary and sufficient
for $A'$ to be regular $(0_{IV}, 17.1.1)$.

**Remarks (22.5.2).**

<!-- label: 0_IV.22.5.2 -->

*(i) Let $A_{1} = A/\mathfrak{m}^{2}$, $A'_{1} = A' \otimes_{A} A_{1} = A'/\mathfrak{m}^{2} A'$; since $\mathfrak{m}^{2}
A' \subset \mathfrak{m}'^{2}$, $\mathfrak{m}'_{1} = \mathfrak{m}'/\mathfrak{m} A'$ is the maximal ideal of $A'_{1}$ and
$\mathfrak{m}'_{1}/\mathfrak{m}'^{2}_{1}$ is a $K'$-vector space isomorphic to $\mathfrak{m}'/\mathfrak{m}'^{2}$; the
regularity condition for $A'$ therefore depends only on the structure of the `A_1`-algebra $A'_{1}$, which will allow us
below to apply the preliminary results of `(22.4)` on the finite algebras over Artinian rings.*

*(ii) It results from the proof of `(22.5.1)` and from $(0_{IV}, 16.2.6.1)$ that one has in any case*

$$ (22.5.2.1) rg_{K}(\mathfrak{m}/\mathfrak{m}^{2}) \leq rg_{K'}(\mathfrak{m}'/\mathfrak{m}'^{2}). $$

<!-- original page 202 -->

*(iii) Suppose that $A$ and $A'$ satisfy the general hypotheses of `(22.4.1)`. One knows $(0_{IV}, 19.8.10)$ that there
exists a regular local ring $B$, of maximal ideal $\mathfrak{n}$, such that $A$ is isomorphic to $B/\mathfrak{n}^{2}$;
let $G_{i} \in B[T_{i}]$ be a unitary polynomial whose canonical image in $A[T_{i}]$ is $F_{i}$ ($1 \leq i \leq r$);
then, if $B'$ is the quotient ring of $B[T_{1}, \cdots, T_{r}]$ by the ideal generated by the $G_{i}$, it is clear that
$B'$ is a free $B$-module of rank $d$ and that $A' = B' \otimes_{B} A = B'/\mathfrak{n}^{2} B'$; since $A'$ is supposed
to be a local ring, so is $B'$, and if $\mathfrak{n}'$ is the maximal ideal of $B'$, $B'/\mathfrak{n}'$ is isomorphic to
$K'$ and $\mathfrak{n}'/\mathfrak{n}'^{2}$ isomorphic to $\mathfrak{m}'/\mathfrak{m}'^{2}$ as vector space over $K'$;
the inequality `(22.5.2.1)` therefore shows that under the hypotheses of `(22.4.1)`*

$$ (22.5.2.2) rg_{K}(V) \leq rg_{K'}(\mathfrak{m}'/\mathfrak{m}'^{2}). $$

**Corollary (22.5.3).**

<!-- label: 0_IV.22.5.3 -->

*Let $A$ be a regular local ring, $\mathfrak{m}$ its maximal ideal, $T_{i}$ ($1 \leq i \leq r$) indeterminates, and for
each $i$, let*

```text
  (22.5.3.1)   F_i(T_i) = T_i^{d_i} + ∑_{1 ≤ k ≤ d_i} c_{ik} T_i^{d_i − k}
```

*be a unitary polynomial of $A[T_{i}]$, such that $d_{i} \geq 2$ for every $i$ and $c_{ik} \in \mathfrak{m}$. Let $A'$
be the quotient of the polynomial ring $A[T_{1}, \cdots, T_{r}]$ by the ideal generated by the $r$ polynomials $F_{i}$.
Then:*

*(i) $A'$ is a local ring, and its residue field $K'$ is isomorphic to the residue field $K$ of $A$.*

*(ii) For $A'$ to be a regular ring, it is necessary and sufficient that the classes $\xi_{i}$ mod. $\mathfrak{m}^{2}$
of the elements $c_{i, d_{i}}$ ($1 \leq i \leq r$) be linearly independent over $K$.*

Indeed, with the notations of `(22.5.2, (i))`, if $\bar{F}_{i}$ denotes the polynomial of $A_{1}[T_{i}]$ obtained by
applying to the coefficients of $F_{i}$ the homomorphism $A \to A_{1}$, $A'_{1}$ is defined from `A_1` and the
polynomials $\bar{F}_{i}$ as in `(22.4.1)`, and the conclusion therefore results from `(22.5.1)` and `(22.4.3)`.

**Theorem (22.5.4).**

<!-- label: 0_IV.22.5.4 -->

*Let $A$ be a regular local ring, $K$ its residue field; suppose that $K$ is of characteristic $p > 0$; let*

```text
  (22.5.4.1)   F_i(T_i) = T_i^p + p ∑_{k=1}^{p−1} c_{ik} T_i^{p−k} − f_i
```

*with $c_{ik} \in A$ and $f_{i} \in A$ ($1 \leq i \leq r$); let $B$ be the quotient ring of $A[T_{1}, \cdots, T_{r}]$ by
the ideal generated by the $r$ polynomials $F_{i}$. Then $B$ is a local ring, and the following conditions are
equivalent:*

*a) $B$ is regular;*

*b) the elements $d_{A} f_{i} \otimes 1_{K}$ ($1 \leq i \leq r$) are linearly independent in the $K$-vector space
$\Omega^{1}_{A} \otimes_{A} K$;*

*c) if $B' = B/\mathfrak{m}^{2} B$ and if one sets $\Xi_{B_{(K)}/K} = \Xi_{B'_{(K)}/K}$ `(22.4.5)`, the characteristic
homomorphism $\Xi_{B_{(K)}/K} \to \mathfrak{m}'/\mathfrak{m}'^{2}$ `(22.4.6.2)` is injective.*

Indeed, $B'$ is again defined from $A_{1} = A/\mathfrak{m}^{2}$ and the polynomials $\bar{F}_{i}$ obtained by applying
to the $F_{i}$ the homomorphism $A \to A_{1}$. Taking account of the fact that $\Omega^{1}_{A_{1}} \otimes_{A_{1}} K$ is
canonically isomorphic to $\Omega^{1}_{A} \otimes_{A} K$ $(0_{IV}, 20.5.12, (ii))$, the theorem results from `(22.5.1)`
and `(22.4.7.4)`, using remark `(22.4.8)` when `A_1` is not of characteristic $p$.

<!-- original page 203 -->

(22.5.5) Let $k$ be a field of characteristic $p > 0$, $A$ a local ring, $k'$ a finite radicial extension of $k$ such
that $k'^{p} \subset k$, $\mathfrak{m}$ the maximal ideal of $A$, $K = A/\mathfrak{m}$ its residue field; recall that
$A' = A \otimes_{k} k'$ is a local ring whose residue field is the same as that of the local ring $K \otimes_{k} k'$
(Bourbaki, *Alg. comm.*, chap. V, §2, n° 3, lemma 4). Note that one has $A'_{(K)} = A' \otimes_{A'} K = K \otimes_{k}
k'$, and consequently $(0_{IV}, 21.3.6)$

```text
  (22.5.5.1)   Θ_{A′_{(K)}/K} = Θ_{k′/k} ⊗_k K
```

up to a canonical isomorphism. Moreover, one knows $(0_{IV}, 21.4.7)$ that one has $\Xi_{k'/k} = 0$, in other words the
canonical homomorphism $(0_{IV}, 21.3.2.2)$

$$ \pi_{k'/k} : \Theta_{k'/k} \to \Omega^{1}_{k} $$

is injective, so one has a canonical injection

```text
  (22.5.5.2)   Θ_{A′_{(K)}/K} → Ω^1_k ⊗_k K
```

which is made explicit as follows (taking account of `(22.5.5.1)`): for every $x' \in k'$, to the element
$d_{A'_{(K)}/K}(x' \otimes 1_{K}) \otimes 1_{K}$ of $\Omega^{1}_{A'_{(K)}/A'_{(K)}} K$, one makes correspond the element
$d_{k}(x'^{p}) \otimes 1_{K}$ of $\Omega^{1}_{k} \otimes_{k} K$.

**Lemma (22.5.6).**

<!-- label: 0_IV.22.5.6 -->

*With the notations of `(22.5.5)`:*

*(i) The kernel of the canonical homomorphism $\pi_{A'_{(K)}/K}$ $(0_{IV}, 21.3.2.2)$ identifies via `(22.5.5.2)` with
$(\Theta_{k'/k} \otimes_{k} K) \cap \Upsilon_{K/k}$.*

*(ii) Let $A_{1} = A/\mathfrak{m}^{2}$, $A'_{1} = A_{1} \otimes_{k} k' = A'/\mathfrak{m}^{2} A'$; then the
characteristic homomorphism $\chi'_{A'_{1}/A_{1}}$ `(22.4.6.2)` identifies with the restriction of the characteristic
homomorphism $\chi_{A/k} : \Upsilon_{K/k} \to V = \mathfrak{m}/\mathfrak{m}^{2}$ $(0_{IV}, 20.6.24)$ to $(\Theta_{k'/k}
\otimes_{k} K) \cap \Upsilon_{K/k}$.*

(i) By virtue of $(0_{IV}, 20.6.9)$, applied by replacing $\Lambda$ by the prime field, $B$ by $k$, $C$ by $K$ and $E$
by $A_{1} = A/\mathfrak{m}^{2}$ (extension of $K$ by $V = \mathfrak{m}/\mathfrak{m}^{2}$), it suffices (cf. `(22.5.5)`)
to verify that if $x' \in k'$ and if $y \in A_{1}$ is an element whose class mod. $\mathfrak{m}/\mathfrak{m}^{2}$ is
$x'^{p} \in k$, then the image of $d_{k}(x'^{p}) \otimes 1_{K}$ by the canonical homomorphism $\Omega^{1}_{k}
\otimes_{k} K \to \Omega^{1}_{A} \otimes_{A} K$ is $d_{A} z \otimes 1_{K}$, which results from the definitions.

(ii) Since $A'_{(K)} = K \otimes_{k} k' = (A'_{1})_{(K)}$ (by virtue of the relation $K =
A_{1}/(\mathfrak{m}/\mathfrak{m}^{2})$), $\Theta_{A'_{1}/k}$ identifies with $\Theta_{A'_{(K)}/K}$, and the verification
results from the same calculation as in (i) and from the definition `(22.4.5.2)` of $\pi'_{(A'_{1})_{(K)}/K}$.

**Proposition (22.5.7).**

<!-- label: 0_IV.22.5.7 -->

*Let $k$ be a field of characteristic $p > 0$, $A$ a $k$-algebra which is a regular local ring, $\mathfrak{m}$ its
maximal ideal, $K = A/\mathfrak{m}$ its residue field; let $V = \mathfrak{m}/\mathfrak{m}^{2}$, regarded as a $K$-vector
space. Let $k'$ be a finite extension of $k$ such that $k'^{p} \subset k$, and $A' = A \otimes_{k} k'$; for the local
ring $A'$ to be regular, it is necessary and sufficient that the restriction of the characteristic homomorphism
$\chi_{A/k} : \Upsilon_{K/k} \to V$ $(0_{IV}, 20.6.24)$ to $(\Theta_{k'/k} \otimes_{k} K) \cap \Upsilon_{K/k}$ be
injective.*

It is required to prove that the condition of the statement is equivalent to `(22.5.1.1)`, denoting by $\mathfrak{m}'$
the maximal ideal of $A'$, by $K' = A'/\mathfrak{m}'$ its residue field. With the notations of remark `(22.5.2, (i))`,
one has $A'_{1} = A_{1} \otimes_{k} k'$. Now, let $(a_{i})_{1 \leq i \leq r}$ be a $p$-basis of $k'$ over $k$, so that
$a^{p}_{i} = b_{i} \in k$, and $k'$ is isomorphic to the quotient of the polynomial ring

<!-- original page 204 -->

$k[T_{1}, \cdots, T_{r}]$ by the ideal generated by the polynomials $F_{i} = T^{p}_{i} - b_{i}$ ($1 \leq i \leq r$); one
deduces that $A'_{1}$ is isomorphic to the quotient of the polynomial ring $A_{1}[T_{1}, \cdots, T_{r}]$ by the ideal
generated by the $F_{i}$. One may then apply the criterion `(22.4.7)`, and the condition of the statement therefore
amounts to the fact that $\chi'_{A'_{1}/A_{1}}$ is injective; one concludes with the aid of `(22.5.6)`.

We can now prove the converse of $(0_{IV}, 19.6.5)$:

**Theorem (22.5.8).**

<!-- label: 0_IV.22.5.8 -->

*Let $k$ be a field, $p$ its characteristic exponent, $A$ a Noetherian local $k$-algebra. The following conditions are
equivalent:*

*a) $A$ is a $k$-algebra formally smooth (for its preadic topology).*

*b) $A$ is geometrically regular over $k$.*

*b′) For every finite extension $k'$ of $k$ such that $k'^{p} \subset k$, $A' = A \otimes_{k} k'$ is a regular ring.*

Taking account of $(0_{IV}, 19.6.6)$, one may reduce to the case $p > 1$.

The fact that a) implies b) is none other than $(0_{IV}, 19.6.5)$, and b) trivially entails b′). We show that b′)
entails that the conditions of `(22.2.2)` are satisfied; this is evident for the first $(0_{IV}, 17.1.1)$ since b′)
implies first that $A$ is regular. On the other hand, let $(x_{\alpha})_{\alpha \in I}$ be a $p$-basis of $k^{1/p}$ over
$k$; one knows that the elements $d_{k}(x^{p}_{\alpha})$ form a basis of the $k$-vector space $\Omega^{1}_{k}$ $(0_{IV},
21.4.5)$, hence the elements $d_{k}(x^{p}_{\alpha}) \otimes 1_{K}$ form a basis of the $K$-vector space $\Omega^{1}_{k}
\otimes_{k} K$. One concludes (cf. `(22.5.5)`) that when $k'$ runs through the set of subextensions of $k^{1/p}$, finite
over $k$, the family of subspaces $\Theta_{k'/k} \otimes_{k} K$ of $\Omega^{1}_{k} \otimes_{k} K$ is filtering
increasing and has for union $\Omega^{1}_{k} \otimes_{k} K$. It follows then from `(22.5.7)` that condition b′) entails
that $\chi_{A/k}$ is injective, which is none other than condition (ii) of `(22.2.2)`.

**Corollary (22.5.9).**

<!-- label: 0_IV.22.5.9 -->

*Let $k$ be a field, $A$ a Noetherian local $k$-algebra formally smooth. Then, for every prime ideal $\mathfrak{p}$ of
$A$, the local ring $A_{\mathfrak{p}}$ is a $k$-algebra formally smooth (for the $\mathfrak{p}$-preadic topology).*

Indeed, with the notations of $(22.5.8, b')$, it suffices to show that the local ring $A_{\mathfrak{p}} \otimes_{k} k'$
is regular; but as it is a ring of fractions of the local ring $A \otimes_{k} k'$ and the latter is regular by
hypothesis, the same holds of $A_{\mathfrak{p}} \otimes_{k} k'$ $(0_{IV}, 17.3.6)$.

**Remarks (22.5.10).**

<!-- label: 0_IV.22.5.10 -->

*(i) The conclusion of `(22.5.8)` is in default when, in condition b′), one restricts to monogenic extensions $k' =
k(x)$ of $k$ (with $x^{p} \in k$). It may indeed happen that for *all* these extensions $k'$, one has $\Upsilon_{K/k}
\cap (\Theta_{k'/k} \otimes_{k} K) = 0$, even though $\Upsilon_{K/k} \neq 0$; this means that for every $x \in k^{1/p}$
such that $x \notin k$, one must have $d_{k}(x^{p}) \otimes 1 \notin \Upsilon_{K/k}$, or equivalently $d_{K}(x^{p}) \neq
0$, that is to say $x^{p} \notin K^{p}$; in other words, one must have $K^{p} \cap k = k^{p}$, even though $K$ be an
inseparable extension of $k$. Now, one easily constructs examples of such extensions: start from a perfect field $k_{0}$
of characteristic $p > 0$, let $X$, $Y$, $Z$ be three indeterminates and set $k = k_{0}(X, Y)$ and $K = k(X^{1/p} + Z
Y^{1/p})$; one easily verifies that $K$ satisfies the preceding conditions, hence $\Upsilon_{K/k} \neq 0$. Apply now the
lemma `(22.2.5.2)` taking $V = K$ and for $h$ the zero homomorphism; $A$ is then a discrete valuation ring having $K$
for residue field, with $\chi_{A/k} = 0$, and is therefore not a $k$-algebra formally smooth by `(22.2.2)`; however $A
\otimes_{k} k'$ is a regular ring for every monogenic extension $k' \subset k^{1/p}$ of $k$.*

<!-- original page 205 -->

*(ii) The corollary `(22.5.9)` leads to consideration of the following question: if $A$ is a Noetherian $k$-algebra,
under what conditions is the set of prime ideals $\mathfrak{p} \in \operatorname{Spec}(A)$ such that $A_{\mathfrak{p}}$
is a $k$-algebra formally smooth open? We shall address certain particular cases of this later.*

### 22.6. Zariski's Jacobian criterion

**Theorem (22.6.1)** (Jacobian criterion of formal smoothness).

<!-- label: 0_IV.22.6.1 -->

*Let $A$, $B$ be two topological rings, $u : A \to B$ a continuous homomorphism making $B$ a $A$-algebra formally
smooth, $\mathfrak{J}$ an ideal of $B$ (not necessarily closed), $C = B/\mathfrak{J}$ the quotient topological
$A$-algebra. For $C$ to be a $A$-algebra formally smooth, it is necessary and sufficient that the canonical homomorphism
(cf. $(0_{IV}, 20.5.11.2)$)*

```text
  (22.6.1.1)   δ_{C/B/A} : 𝔍/𝔍² → Ω^1_{B/A} ⊗_B C
```

*be formally left-invertible (cf. $(0_{IV}, 19.1.5)$).*

Indeed, to say that $B$ (resp. $C$) is a $A$-algebra formally smooth signifies $(0_{IV}, 19.4.4)$ that one has
$Exalcotop_{A}(B, L) = 0$ (resp. $Exalcotop_{A}(C, L) = 0$) for every discrete $B$-module (resp. $C$-module) $L$
annihilated by an open ideal of $B$ (resp. $C$). Since by hypothesis $Exalcotop_{A}(B, L) = 0$ for every discrete
$C$-module $L$ annihilated by an open ideal of $C$, to say that $C$ is a $A$-algebra formally smooth therefore signifies
that the canonical homomorphism $Exalcotop_{A}(C, L) \to Exalcotop_{A}(B, L)$ is injective, and the theorem results from
$(0_{IV}, 20.7.8)$.

Recall $(0_{IV}, 19.5.3)$ that when $B$ and $C$ are $A$-algebras formally smooth, $\mathfrak{J}/\mathfrak{J}^{2}$ is a
formally projective topological $C$-module; moreover, the canonical homomorphisms $\phi_{n} :
S^{n}_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to \mathfrak{J}^{n}/\mathfrak{J}^{n+1}$ are formal bimorphisms when $B$ is
supposed to be a preadmissible ring.

**Corollary (22.6.2).**

<!-- label: 0_IV.22.6.2 -->

*The hypotheses and notations being those of `(22.6.1)`, suppose moreover that in $B$ the square of every open ideal is
open, and that on $\mathfrak{J}$ the topology induced by that of $B$ is identical to the topology deduced from that of
$B$ $(0_{IV}, 19.0)$ (note that these two conditions are satisfied when $B$ is Noetherian and its topology preadic
$(0_{I}, 7.3.2)$, or if the topology of $B$ is the $\mathfrak{J}$-preadic topology). Let $(\mathfrak{b}_{\lambda})$ be a
fundamental system of open ideals of $B$ and set $B_{\lambda} = B/\mathfrak{b}_{\lambda}$ for every $\lambda$. Then:*

*(i) The following conditions are equivalent:*

*a) $C$ is a $A$-algebra formally smooth.*

*b) For every $\lambda$, the homomorphism of $B_{\lambda}$-modules*

```text
  (22.6.2.1)   (𝔍/𝔍²) ⊗_B B_λ → Ω^1_{B/A} ⊗_B B_λ
```

*deduced from $\delta_{C/B/A}$ by tensorisation, is left-invertible (in other words an isomorphism onto a direct factor
of $\Omega^{1}_{B/A} \otimes_{B} B_{\lambda}$).*

*(ii) Suppose moreover that the topological ring $C$ is preadmissible $(0_{I}, 7.1.2)$ and*

<!-- original page 206 -->

*let $\mathfrak{L}$ be an ideal of definition of $C$; then conditions a) and b) of (i) are equivalent also to:*

*c) The homomorphism of $(C/\mathfrak{L})$-modules*

```text
  (𝔍/𝔍²) ⊗_C (C/𝔏) → Ω^1_{B/A} ⊗_B (C/𝔏)
```

*is left-invertible.*

The hypotheses entail that on $\Omega^{1}_{B/A}$ the topology is deduced from that of $B$ $(0_{IV}, 20.4.5)$, hence (i)
results from `(22.6.1)` and $(0_{IV}, 19.1.7)$. On the other hand, recall $(0_{IV}, 20.4.9)$ that since $B$ is a
$A$-algebra formally smooth, $\Omega^{1}_{B/A}$ is a formally projective $B$-module, hence $\Omega^{1}_{B/A} \otimes_{B}
B_{\lambda}$ is a projective $B_{\lambda}$-module for every $\lambda$ $(0_{IV}, 19.2.4)$; the equivalence of c) with a)
and b) when $C$ is preadmissible then results from $(0_{IV}, 19.1.9)$.

In particular:

**Corollary (22.6.3).**

<!-- label: 0_IV.22.6.3 -->

*Let $A$ be a ring, $B$ a $A$-algebra, $\mathfrak{J}$ an ideal of $B$, $C = B/\mathfrak{J}$; suppose $A$, $B$, $C$
equipped with the discrete topologies and that $B$ is a $A$-algebra formally smooth. For $C$ to be a $A$-algebra
formally smooth, it is necessary and sufficient that the canonical homomorphism `(22.6.1.1)` be left-invertible.*

Note that since every $A$-algebra $C$ is a quotient of a polynomial algebra $A[T_{\alpha}]_{\alpha \in I}$, and the
latter is formally smooth $(0_{IV}, 19.3.3)$, the criterion `(22.6.3)` permits in principle to recognize whether $C$ is
a $A$-algebra formally smooth.

**Proposition (22.6.4).**

<!-- label: 0_IV.22.6.4 -->

*Let $A$ be a ring, $B$ a $A$-algebra formally smooth (for the discrete topologies), $\mathfrak{J}$ an ideal of $B$, $C
= B/\mathfrak{J}$; suppose that $\mathfrak{J}/\mathfrak{J}^{2}$ is a $C$-module of finite type. Let $\mathfrak{p}$ be a
prime ideal of $C$, $k(\mathfrak{p})$ the residue field of $C_{\mathfrak{p}}$, $\mathfrak{p}'$ the inverse image of
$\mathfrak{p}$ in $B$, $\mathfrak{q}$ the prime ideal of $A$ inverse image of $\mathfrak{p}'$. The following conditions
are equivalent:*

*a) $C_{\mathfrak{p}}$ is a $A_{\mathfrak{q}}$-algebra formally smooth (for the discrete topologies).*

*a′) $C_{\mathfrak{p}}$ is a $A$-algebra formally smooth (for the discrete topologies).*

*b) The canonical homomorphism*

```text
  (22.6.4.1)   (𝔍/𝔍²) ⊗_C k(𝔭) → Ω^1_{B/A} ⊗_B k(𝔭)
```

*is injective.*

*c) There exists $f \in C - \mathfrak{p}$ such that $C_{f}$ is a $A$-algebra formally smooth.*

*If moreover $B$ is Noetherian, the preceding conditions are also equivalent to*

*d) $C_{\mathfrak{p}}$ is a $A_{\mathfrak{q}}$-algebra formally smooth for the $\mathfrak{p}$-preadic topology on
$C_{\mathfrak{p}}$ and the discrete topology (or the $\mathfrak{q}$-preadic topology) on $A_{\mathfrak{q}}$.*

Since $A_{\mathfrak{q}}$ is a $A$-algebra formally smooth $(0_{IV}, 19.3.5, (iv) and (ii))$, one already knows that a)
and a′) are equivalent $(0_{IV}, 19.3.5, (ii))$. One has $C_{\mathfrak{p}} = B_{\mathfrak{p}'}/\mathfrak{J}
B_{\mathfrak{p}'}$ and $B_{\mathfrak{p}'}$ is a $A$-algebra formally smooth for the discrete topology $(0_{IV}, 19.3.5,
(iv))$; moreover $\Omega^{1}_{B_{\mathfrak{p}'}/A} = (\Omega^{1}_{B/A})_{\mathfrak{p}'}$ $(0_{IV}, 20.5.9)$. The
equivalence of a′) and b) then results from the application of `(22.6.3)` to $B_{\mathfrak{p}'}$ and $C_{\mathfrak{p}}$,
taking account of the fact that $\Omega^{1}_{B/A}$ is a projective $B$-module ($(0_{IV}, 20.4.9)$ and $(0_{IV},
19.2.1)$) and $\mathfrak{J}/\mathfrak{J}^{2}$ a $B$-module of finite type, and using $(0_{IV}, 19.1.12)$. The
application of $(0_{IV}, 19.1.12)$ also proves the equivalence of b) and c). Finally, note that since
$B_{\mathfrak{p}'}$ is a $A_{\mathfrak{q}}$-algebra formally smooth for the discrete topologies

<!-- original page 207 -->

$(0_{IV}, 19.3.5, (iv))$, $B_{\mathfrak{p}'}$, equipped with the $\mathfrak{p}'$-preadic topology, is still a
$A_{\mathfrak{q}}$-algebra formally smooth when one takes on $A_{\mathfrak{q}}$ the discrete topology or the
$\mathfrak{q}$-preadic topology $(0_{IV}, 19.3.8)$. To show the equivalence of b) and d) when $B$ is Noetherian, apply
`(22.6.2)` to the ring $A_{\mathfrak{q}}$ discrete (or $\mathfrak{q}$-preadic) and to the ring $B_{\mathfrak{p}'}$,
equipped with the $\mathfrak{p}'$-preadic topology; since $C_{\mathfrak{p}}$ is preadmissible and $\mathfrak{p}
C_{\mathfrak{p}}$ is an ideal of definition for its topology, one may invoke the equivalence of c) and a) in `(22.6.2)`.

**Corollary (22.6.5).**

<!-- label: 0_IV.22.6.5 -->

*Under the general hypotheses of `(22.6.4)`, the set of $\mathfrak{p} \in \operatorname{Spec}(C)$ such that
$C_{\mathfrak{p}}$ is a $A$-algebra formally smooth (or a $A_{\mathfrak{q}}$-algebra formally smooth, denoting by
$\mathfrak{q}$ the inverse image of $\mathfrak{p}$ in $A$) for the discrete topologies, is open in
$\operatorname{Spec}(C)$.*

This results from form c) of `(22.6.4)`. Note that when $B$ is Noetherian, one may replace the discrete topologies by
the preadic topologies.

**Corollary (22.6.6).**

<!-- label: 0_IV.22.6.6 -->

*Under the general hypotheses of `(22.6.4)`, the following conditions are equivalent:*

*a) $C$ is a $A$-algebra formally smooth (for the discrete topologies).*

*b) For every $\mathfrak{p} \in \operatorname{Spec}(C)$ (or only for every maximal ideal $\mathfrak{p}$ of $C$),
$C_{\mathfrak{p}}$ is a $A$-algebra formally smooth (or a $A_{\mathfrak{q}}$-algebra formally smooth, denoting by
$\mathfrak{q}$ the inverse image of $\mathfrak{p}$ in $A$) for the discrete topologies.*

*Moreover, when $B$ is Noetherian, one may in b) replace the discrete topologies by the preadic topologies on
$A_{\mathfrak{q}}$ and $C_{\mathfrak{p}}$.*

The last assertion results from `(22.6.4)`. By virtue of `(22.6.3)`, condition a) amounts to the fact that the
homomorphism `(22.6.1.1)` is left-invertible; the equivalence of a) and b) therefore results from $(0_{IV}, 19.1.14)$,
taking account of the fact that $\Omega^{1}_{B/A}$ is a projective $B$-module and $\mathfrak{J}/\mathfrak{J}^{2}$ a
$C$-module of finite type.

**Proposition (22.6.7).**

<!-- label: 0_IV.22.6.7 -->

*Let $k_{0}$ be a field, $k$ a separable extension of $k_{0}$, $C$ a $k$-algebra of finite type.*

*(i) Let $\mathfrak{p}$ be a prime ideal of $C$. The following conditions are equivalent:*

*a) $C_{\mathfrak{p}}$ is a $k_{0}$-algebra formally smooth for the discrete topology.*

*b) $C_{\mathfrak{p}}$ is a $k_{0}$-algebra formally smooth for the $\mathfrak{p}$-preadic topology.*

*c) There exists $f \in C - \mathfrak{p}$ such that $C_{f}$ is a $k_{0}$-algebra formally smooth for the discrete
topology.*

*d) $C_{\mathfrak{p}}$ is a geometrically regular ring $(0_{IV}, 19.6.5)$ over $k_{0}$.*

*Moreover the set of $\mathfrak{p} \in \operatorname{Spec}(C)$ having any one of these properties is open in
$\operatorname{Spec}(C)$.*

*(ii) The following conditions are equivalent:*

*a) $C$ is a $k_{0}$-algebra formally smooth for the discrete topology.*

*b) Every $\mathfrak{p} \in \operatorname{Spec}(C)$ satisfies the equivalent conditions of (i).*

*c) Every maximal ideal $\mathfrak{m}$ of $C$ satisfies the equivalent conditions of (i).*

*d) For every extension $k'$ of $k_{0}$, $C \otimes_{k_{0}} k'$ is a regular ring $(0_{IV}, 17.3.6)$; one says again
that $C$ is a geometrically regular ring over $k_{0}$.*

<!-- original page 208 -->

*(iii) Let $B = k[T_{1}, \cdots, T_{r}]$ be a polynomial algebra, $\mathfrak{J}$ an ideal of $B$ such that $C$ is
isomorphic to $B/\mathfrak{J}$. Let $\mathfrak{q}$ be a prime ideal of $B$ containing $\mathfrak{J}$ and set
$\mathfrak{p} = \mathfrak{q}/\mathfrak{J}$. The conditions of (i) are then still equivalent to the following ("Zariski's
Jacobian criterion"):*

*e) There exists a system of elements $(f_{i})_{1 \leq i \leq m}$ of $\mathfrak{J}$, generating the ideal
$\mathfrak{J}_{\mathfrak{q}}$ in $B_{\mathfrak{q}}$, and $k_{0}$-derivations $D_{j}$ of $B$ into itself ($1 \leq j \leq
m$) such that $det(D_{j}(f_{i})) \notin \mathfrak{q}$.*

One knows that $C$ is always isomorphic to a $k$-algebra of the form $B/\mathfrak{J}$. Since $B$ is a $k$-algebra
formally smooth $(0_{IV}, 19.3.3)$ and $k$, being separable over $k_{0}$, is a $k_{0}$-algebra formally smooth $(0_{IV},
19.6.1)$, $B$ is a $k_{0}$-algebra formally smooth $(0_{IV}, 19.3.5, (ii))$. The equivalence of conditions a), b), c) of
(i) therefore results from `(22.6.4)`, and that of a), b), c) in (ii) results from `(22.6.6)`; the equivalence of a) and
d) in (i) results from `(22.5.8)`; since every localization of $C \otimes_{k_{0}} k'$ is also a localization of
$C_{\mathfrak{p}} \otimes_{k_{0}} k'$ for a suitable prime ideal $\mathfrak{p} \in \operatorname{Spec}(C)$, the
equivalence of d) and b) in (ii) results from the equivalence of d) and a) in (i). Finally, since $\Omega^{1}_{B/k_{0}}$
is a projective $B$-module, the equivalence of Zariski's criterion e) and the other conditions of (i) follows from
$(0_{IV}, 19.1.12)$ and `(22.6.3)`, taking account of $(0_{IV}, 20.4.8)$.

Zariski was in fact interested in a differential criterion of *regularity* for the local rings $C_{\mathfrak{p}}$. Since
it amounts to the same to say that a Noetherian local ring containing a field is regular or is formally smooth as
algebra over its prime subfield $(0_{IV}, 19.6.4)$, one obtains at once such a criterion by replacing $k_{0}$ by the
prime subfield of $k$ in `(22.6.7)`; in particular, one obtains the following result, which we shall later find again
`(IV, 6.12.5)` as a particular case of more general results of Nagata:

**Corollary (22.6.8)** (Zariski).

<!-- label: 0_IV.22.6.8 -->

*Let $C$ be a finite-type algebra over a field. Then the set of $\mathfrak{p} \in \operatorname{Spec}(C)$ such that
$C_{\mathfrak{p}}$ is a regular local ring is open in $\operatorname{Spec}(C)$.*

**Remarks (22.6.9).**

<!-- label: 0_IV.22.6.9 -->

*(i) The statements of `(22.6.7)` are still valid if instead of supposing $k$ separable over $k_{0}$, one supposes only
that it is of finite radicial multiplicity, in other words $(0_{IV}, 19.6.6)$ that there exists a finite radicial
extension $k'_{0}$ of $k_{0}$ such that the residue field of the local Artinian ring $k \otimes_{k_{0}} k'_{0}$ is a
separable extension $k'$ of $k'_{0}$. There then exists a $k_{0}$-monomorphism $k' \to k \otimes_{k_{0}} k'_{0}$ which,
composed with the canonical homomorphism $k \otimes_{k_{0}} k'_{0} \to k'$, gives the identity, since $k'$ is a
$k'_{0}$-algebra formally smooth $(0_{IV}, 19.6.1)$; one concludes that $C \otimes_{k_{0}} k'_{0}$ is equipped with a
structure of $k'$-algebra of finite type, and since $k'$ is separable over $k'_{0}$, one may apply `(22.6.7)` to this
$k'$-algebra; one concludes our assertion by applying $(0_{IV}, 19.4.7)$. Since we shall not have to make use of this
generalization, we leave the detail to the reader. We do not know on the other hand whether the results of `(22.6.7)`
are valid without any hypothesis on the extension $k$ of $k_{0}$.*

*(ii) Under the general hypotheses of `(22.6.7)`, let $(k_{\alpha})$ be a decreasing filtered family of subfields of $k$
containing $k_{0}$ and such that $\bigcap_{\alpha} k_{\alpha}(k^{p}) = k_{0}(k^{p})$ (where $p$ is the characteristic
exponent of $k_{0}$). Using a dimension-counting method due to Nagata, one can show that, in the Jacobian criterion
`(22.6.7, (iii))`, one may restrict to derivations $D_{j}$ of $B$ which are $k_{\alpha}$-derivations for a suitable
$\alpha$.*

<!-- original page 209 -->

*The interest of this result is that there are always such families $(k_{\alpha})$ for which $[k : k_{\alpha}]$ is
finite $(0_{IV}, 21.8.6)$. We shall not prove this refinement of Zariski's criterion, of which we shall not have to make
use. In `(22.7)`, we shall give, for complete local rings, a variant (also due to Nagata) of Zariski's criterion, which
is proved essentially by the same method (with somewhat greater technical difficulties).*

### 22.7. Nagata's Jacobian criterion

(22.7.1) Nagata's Jacobian criterion is the analogue of Zariski's Jacobian criterion, but for quotient rings of rings of
formal series over a field. We shall give, like Nagata `[31]`, two versions, presented here as criteria of formal
smoothness.

**Proposition (22.7.2).**

<!-- label: 0_IV.22.7.2 -->

*Let $k$ be a field, $A = k[[T_{1}, \cdots, T_{r}]]$ a ring of formal series over $k$, equipped with its usual structure
of $k$-algebra, $\mathfrak{q}$ an ideal of $A$, $B = A/\mathfrak{q}$. Let $\mathfrak{p}$ be a prime ideal of $A$
containing $\mathfrak{q}$. Suppose there exists a sub-$k$-algebra $C'$ of $C = A/\mathfrak{p}$, isomorphic to an algebra
of formal series $k[[X_{1}, \cdots, X_{s}]]$, such that $C$ is finite over $C'$ and that the field of fractions $L$ of
$C$ is a separable extension of $L' = k((X_{1}, \cdots, X_{s}))$ (hypothesis always satisfied if $k$ is of
characteristic `0`). Then the following conditions are equivalent:*

*a) $B_{\mathfrak{p}} = A_{\mathfrak{p}}/\mathfrak{q} A_{\mathfrak{p}}$ is a $k$-algebra formally smooth for the
$\mathfrak{p}$-preadic topology.*

*b) There exist $k$-derivations $D_{i}$ ($1 \leq i \leq m$) of $A$ into itself, and elements $f_{i}$ ($1 \leq i \leq m$)
of $\mathfrak{q}$, such that the images of the $f_{i}$ in $\mathfrak{q} A_{\mathfrak{p}}$ generate this ideal of
$A_{\mathfrak{p}}$, and that one has $det(D_{i} f_{j}) \notin \mathfrak{p}$.*

*c) $B_{\mathfrak{p}}$ is a regular ring.*

The residue field of $B_{\mathfrak{p}}$ is $k(\mathfrak{p})$; since $k((X_{1}, \cdots, X_{s}))$ is separable over $k$
$(0_{IV}, 21.9.6.4)$, $k(\mathfrak{p})$ is separable over $k$ by hypothesis, and one already knows that under these
conditions properties a) and c) are equivalent $(0_{IV}, 19.6.4)$. Moreover $A_{\mathfrak{p}}$ is a regular ring
($(0_{IV}, 17.1.4)$ and $(0_{IV}, 17.3.2)$), and since its residue field $k(\mathfrak{p})$ is separable over $k$,
$A_{\mathfrak{p}}$ is formally smooth over $k$ for the $\mathfrak{p}$-preadic topology $(0_{IV}, 19.6.4)$. It therefore
results from `(22.6.2, (ii))` that condition a) amounts to the fact that the homomorphism of $L$-vector spaces

```text
  (22.7.2.1)   j_0 : (𝔮/𝔮²) ⊗_A L → Ω^1_{A_𝔭} ⊗_{A_𝔭} L = Ω̂^1_{A/k} ⊗_A L
```

is injective.

Consider on the other hand the composite homomorphism

```text
  (22.7.2.2)   j : (𝔮/𝔮²) ⊗_A L ─j_∗→ Ω^1_{A/k} ⊗_A L → Ω̂^1_{A/k} ⊗_A L
```

and let us show that condition b) is equivalent to saying that $j$ is injective. Note indeed that
$(\mathfrak{q}/\mathfrak{q}^{2}) \otimes_{A} L = (\mathfrak{q} A_{\mathfrak{p}}/\mathfrak{q}^{2} A_{\mathfrak{p}})
\otimes_{A_{\mathfrak{p}}} L$; condition b) signifies that if $F_{i} = j(f'_{i} \otimes 1)$, where $f'_{i}$ is the image
of $f_{i}$ in $\mathfrak{q} A_{\mathfrak{p}}/\mathfrak{q}^{2} A_{\mathfrak{p}}$, the matrix $(\langle F_{i}, D_{j}
\otimes 1\rangle)$ is invertible; hence this entails that the $F_{i}$ are linearly independent, and *a fortiori* the
same holds of the $f'_{i} \otimes 1$; but since these last generate $(\mathfrak{q} A_{\mathfrak{p}}/\mathfrak{q}^{2}
A_{\mathfrak{p}}) \otimes_{A_{\mathfrak{p}}} L$, one concludes that $j$ is injective. Conversely, suppose $j$ injective,
and take the $f_{i}$ such that the $f'_{i} \otimes 1$ form

<!-- original page 210 -->

a basis of $(\mathfrak{q} A_{\mathfrak{p}}/\mathfrak{q}^{2} A_{\mathfrak{p}}) \otimes_{A_{\mathfrak{p}}} L$; then the
$F_{i}$ form a basis of the image of $j$; but one knows $(0_{IV}, 21.9.3)$ that $\hat{\Omega}^{1}_{A/k}$ is a free
$A$-module of rank $r$ and the $k$-derivations of $A$ into itself generate its dual; the fact that the $F_{i}$ are
linearly independent therefore entails the existence of $k$-derivations $D_{j}$ of $A$ into itself such that the matrix
$(\langle F_{i}, D_{j} \otimes 1\rangle)$ be invertible, in other words condition b).

These remarks already show that b) entails a). To prove conversely that condition a) entails that $j$ is injective,
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

*Let $R$ be a regular local ring, $\mathfrak{m}$ its maximal ideal, $K = R/\mathfrak{m}$ its residue field. If
$\mathfrak{n}$ is an ideal of $R$ such that $R/\mathfrak{n}$ is regular, then the canonical homomorphism*

```text
  (22.7.2.5)   α : (𝔫/𝔫²) ⊗_R K → (𝔪/𝔪²) ⊗_R K
```

*is injective.*

Indeed, one knows $(0_{IV}, 17.1.6)$ that $\mathfrak{n}$ is generated by a sequence $(x_{i})_{1 \leq i \leq t}$ forming
part of a regular system of parameters $(x_{i})_{1 \leq i \leq n}$ of $R$; the images of the $x_{i}$ ($1 \leq i \leq t$)
form a basis of $(\mathfrak{n}/\mathfrak{n}^{2}) \otimes_{R} K$, and their images by $\alpha$ form part of the basis of
$(\mathfrak{m}/\mathfrak{m}^{2}) \otimes_{R} K$ formed of the images of the $x_{i}$ for $1 \leq i \leq n$, whence the
lemma.

This lemma and the diagram `(22.7.2.3)` therefore reduce (by virtue of hypothesis a)) to proving that $i$ is injective.
Now, in the sequence

```text
  (22.7.2.6)   𝔭/𝔭² ─h→ Ω̂^1_{A/k} ⊗̂_A (A/𝔭) ─g→ Ω̂^1_{(A/𝔭)/k} → 0
```

one knows $(0_{IV}, 20.7.20)$ that $g$ is surjective and that the image of $h$ is *dense* in the kernel of $g$ for the
$\mathfrak{m}$-adic topology ($\mathfrak{m}$ being the maximal ideal of $A$); since $\hat{\Omega}^{1}_{A/k}$ is an
$A$-module of finite type, all the submodules of the $(A/\mathfrak{p})$-module $\hat{\Omega}^{1}_{A/k} \otimes_{A}
(A/\mathfrak{p}) = \hat{\Omega}^{1}_{A/k} \hat{\otimes}_{A} (A/\mathfrak{p})$ are closed for the $\mathfrak{m}$-adic
topology $(0_{I}, 7.3.5)$, hence the sequence `(22.7.2.6)` is exact. Tensoring by $L$, there arises the exact sequence

```text
  (𝔭/𝔭²) ⊗_A L ─i→ Ω̂^1_{A/k} ⊗_A L → Ω̂^1_{(A/𝔭)/k} ⊗_A L → 0.
```

Now, the hypothesis of separability made on $L$ entails, by virtue of $(0_{IV}, 21.9.5)$, that
$\hat{\Omega}^{1}_{(A/\mathfrak{p})/k} \otimes_{A/\mathfrak{p}} L$ is of rank $s$ over $L$; since
$\hat{\Omega}^{1}_{A/k} \otimes_{A} L$ is of rank $r$ over $L$ $(0_{IV}, 21.9.3)$, one has $rg_{L}(Im(i)) = r - s$. But
since $A/\mathfrak{p}$ is finite over a subalgebra isomorphic to $k[[T_{1}, \cdots, T_{s}]]$, one has
$\dim(A/\mathfrak{p}) = s$ ($(0_{IV}, 17.1.4)$ and $(0_{IV}, 16.1.5)$); hence

```text
  r − s = dim(A) − dim(A/𝔭) = dim(A_𝔭)
```

<!-- original page 211 -->

by $(0_{IV}, 16.5.11)$. Now, since $A_{\mathfrak{p}}$ is regular $(0_{IV}, 17.3.2)$, $\dim(A_{\mathfrak{p}})$ is equal
to the rank over $L$ of $\mathfrak{p} A_{\mathfrak{p}}/\mathfrak{p}^{2} A_{\mathfrak{p}}$ $(0_{IV}, 17.1.1)$, hence to
the rank over $L$ of $(\mathfrak{p}/\mathfrak{p}^{2}) \otimes_{A} L$, which completes proving that $i$ is injective.

**Theorem (22.7.3).**

<!-- label: 0_IV.22.7.3 -->

*Let $k$ be a field, $A$ a complete Noetherian local ring with residue field $K$. Suppose that:*

*1° $[k : k^{p}] < +\infty$ (where $p$ is the characteristic exponent of $k$);*

*2° $K$ is a finite extension of a separable extension `K_0` of $k$;*

*3° $A$ is equipped with a structure of `K_0`-algebra formally smooth (for the preadic topology).*

*Let $\mathfrak{q}$ be an ideal of $A$, $B = A/\mathfrak{q}$, $\mathfrak{p}$ a prime ideal of $A$ containing
$\mathfrak{q}$. The following conditions are equivalent:*

*a) $B_{\mathfrak{p}}$ is a $k$-algebra formally smooth (for the $\mathfrak{p}$-preadic topology).*

*b) There exist $k$-derivations $D_{i}$ of $A$ into itself ($1 \leq i \leq m$) and elements $f_{i}$ ($1 \leq i \leq m$)
of $\mathfrak{q}$, such that the images of the $f_{i}$ in $\mathfrak{q} A_{\mathfrak{p}}$ generate this ideal of
$A_{\mathfrak{p}}$, and that one has $det(D_{i} f_{j}) \notin \mathfrak{p}$.*

*b′) There exists a subextension $k'$ of `K_0`, containing $K^{p}_{0}$, such that $[K_{0} : k'] < +\infty$,
$k'$-derivations $D_{i}$ of $A$ into itself ($1 \leq i \leq m$) and elements $f_{i}$ of $\mathfrak{q}$ ($1 \leq i \leq
m$), such that the images of the $f_{i}$ in $\mathfrak{q} A_{\mathfrak{p}}$ generate this ideal of $A_{\mathfrak{p}}$
and that one has $det(D_{i} f_{j}) \notin \mathfrak{p}$.*

Let us distinguish two cases, according as $p = 1$ or $p > 1$.

A) $k$ is of characteristic `0`. Since $K$ is then a separable extension of `K_0`, it follows from $(0_{IV}, 19.6.4)$
that $A$ is `K_0`-isomorphic to a ring of formal series $K[[T_{1}, \cdots, T_{r}]]$ equipped with its usual structure of
$K$-algebra. But then, taking account of $(0_{IV}, 19.8.8, (ii))$ applied to $A/\mathfrak{p}$, one sees that the general
conditions of `(22.7.2)` are satisfied by replacing therein $k$ by $K$. Moreover, by virtue of $(0_{IV}, 19.6.4)$, it
amounts to the same to say that $B_{\mathfrak{p}}$ is a $k$-algebra formally smooth or a $K$-algebra formally smooth,
the two conditions being equivalent to the fact that $B_{\mathfrak{p}}$ is a regular ring. One may therefore apply the
conclusions of `(22.7.2)`, and it is immediate that this proves the equivalence of a), b) and b′) (with $k' = K_{0}$ in
b′)).

B) $k$ is of characteristic $p > 0$. Since $A$ is a `K_0`-algebra formally smooth and `K_0` is separable over $k$, it
follows from $(0_{IV}, 19.3.5, (ii))$ and $(0_{IV}, 19.6.1)$ that $A$ is a $k$-algebra formally smooth; by virtue of
`(22.5.9)`, $A_{\mathfrak{p}}$ is also a $k$-algebra formally smooth for the $\mathfrak{p}$-preadic topology. It results
then again from `(22.6.2, (ii))` that condition a) amounts to the fact that the homomorphism $j_{0}$ defined in
`(22.7.2.1)` (where $L = k(\mathfrak{p})$) is injective. Hence `(0_IV, 19.1.12, c))` already shows that b) implies a);
since on the other hand b′) trivially implies b), all reduces to showing that the hypothesis that $j_{0}$ is injective
entails b′).

Denote first by $k'$ any subextension of `K_0` such that $[K_{0} : k'] < +\infty$. Note that $\hat{\Omega}^{1}_{A/k'}$
is a free $A$-module of finite type. By the reasoning of `(22.7.2)`, it suffices to show that (for a suitable choice of
$k'$), the composite homomorphism

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

Since $j_{0}$ is injective, one has $Ker(i_{0} \circ \alpha) = 0$. But since $A_{\mathfrak{p}}$ is a regular ring and
hypothesis a) implies that $B_{\mathfrak{p}} = A_{\mathfrak{p}}/\mathfrak{q} A_{\mathfrak{p}}$ is also a regular ring
$(0_{IV}, 19.6.5)$, the lemma `(22.7.2.4)` shows that $\alpha$ is injective, whence $\alpha^{-1}(Ker(i_{0})) = 0$. If
$i'$ is the composite of the homomorphisms of the second line of `(22.7.3.2)`, one has similarly $Ker(j') =
\alpha^{-1}(Ker(i'))$, and all reduces therefore to showing that, for a suitable choice of $k'$, one has

$$ (22.7.3.3) Ker(i') = Ker(i). $$

But the same reasoning as in `(22.7.2)` shows that one has an exact sequence

```text
  (𝔭/𝔭²) ⊗_A L ─i′→ Ω̂^1_{A/k′} ⊗_A L → Ω̂^1_{(A/𝔭)/k′} ⊗_{A/𝔭} L → 0.
```

Now, the hypotheses made permit applying $(0_{IV}, 21.9.8)$, hence there exists a subextension $k'$ of `K_0` containing
$K^{p}_{0}$, such that $[K_{0} : k'] < +\infty$, and for which one has

```text
  rg_L(Ω̂^1_{(A/𝔭)/k′} ⊗_{A/𝔭} L) = dim(A/𝔭) + rg_L Υ_{L/k} + rg_K Ω^1_{K_0/k′}.
```

But one has

```text
  dim(A/𝔭) = dim(A) − dim(A_𝔭)
```

by $(0_{IV}, 16.5.11)$,

```text
  dim(A_𝔭) = rg_L((𝔭/𝔭²) ⊗_A L)
```

since $A_{\mathfrak{p}}$ is regular $(0_{IV}, 17.1.1)$, and finally

```text
  dim(A) + rg_K Ω^1_{K_0/k′} = rg_L(Ω̂^1_{A/k′} ⊗_A L)
```

by virtue of $(0_{IV}, 21.9.2)$; one therefore obtains

$$ (22.7.3.4) rg_{L}(Ker(i')) = rg_{L} \Upsilon_{L/k}. $$

On the other hand, the residue field of $A_{\mathfrak{p}}$ being formally smooth over the prime field of $k$, one has an
exact sequence $(0_{IV}, 20.6.22.1)$

```text
  Υ_{L/k} ─χ_{A_𝔭/k}→ (𝔭 A_𝔭)/(𝔭 A_𝔭)² ─i→ Ω^1_{A_𝔭/k} ⊗_{A_𝔭} L
```

and since $A_{\mathfrak{p}}$ is a $k$-algebra formally smooth for the $\mathfrak{p}$-preadic topology, it follows from
`(22.2.2)` that $\chi_{A_{\mathfrak{p}}/k}$ is an injective homomorphism, hence $Ker(i)$ is isomorphic to
$\Upsilon_{L/k}$, and taking account of `(22.7.3.4)` and the fact that $Ker(i) \subset Ker(i')$, this completes proving
`(22.7.3.3)` and consequently the theorem.

<!-- original page 213 -->

**Remark (22.7.4).**

<!-- label: 0_IV.22.7.4 -->

*One has in fact shown (using $(0_{IV}, 21.9.6)$) that condition b′) is still equivalent to the other conditions of
`(22.7.3)` when one subjects $k'$ to being one of the fields of a decreasing filtered family $(k_{\alpha})$ of subfields
of `K_0` containing $K^{p}_{0}$, such that $[K_{0} : k_{\alpha}] < +\infty$ for every $\alpha$ and $\bigcap_{\alpha}
k_{\alpha} = K^{p}_{0}$.*

**Corollary (22.7.5).**

<!-- label: 0_IV.22.7.5 -->

*Under the general hypotheses of `(22.7.3)`, the set of prime ideals $\mathfrak{n} \in \operatorname{Spec}(B)$ such that
$B_{\mathfrak{n}}$ is a $k$-algebra formally smooth (for the $\mathfrak{n}$-preadic topology) is open in
$\operatorname{Spec}(B)$.*

With the notations of `(22.7.3)`, it suffices to see that if $B_{\mathfrak{p}}$ is formally smooth over $k$, the same
holds for $B_{\mathfrak{p}'}$ for every $\mathfrak{p}' \in V(\mathfrak{q})$ sufficiently close to $\mathfrak{p}$ in
$\operatorname{Spec}(A)$. Now, if the $k$-derivations $D_{i}$ and the elements $f_{i}$ of $\mathfrak{q}$ verify the
criterion b) of `(22.7.3)`, one has also $f = det(D_{i} f_{j}) \notin \mathfrak{p}'$ for $\mathfrak{p}' \in D(f)$; on
the other hand, there exists a $g \notin \mathfrak{p}$ such that the images of the $f_{i}$ in $\mathfrak{q}
A_{\mathfrak{p}'}$ generate $\mathfrak{q} A_{\mathfrak{p}'}$ for $\mathfrak{p}' \in D(g)$ (Bourbaki, *Alg. comm.*, chap.
II, §5, n° 1, prop. 2), which completes proving the corollary.

**Corollary (22.7.6)** (Nagata).

<!-- label: 0_IV.22.7.6 -->

*Let $B$ be a complete Noetherian local ring containing a field. Then the set of $\mathfrak{n} \in
\operatorname{Spec}(B)$ such that $B_{\mathfrak{n}}$ is regular is open in $\operatorname{Spec}(B)$.*

Indeed, $B$ is an algebra over a prime field $k$, hence $(0_{IV}, 19.8.8, (i))$ of the form $A/\mathfrak{q}$, where $A =
K_{0}[[T_{1}, \cdots, T_{r}]]$ is a ring of formal series and `K_0` an extension of $k$; on the other hand, to say that
$B_{\mathfrak{n}}$ is regular amounts to saying that it is a $k$-algebra formally smooth for the $\mathfrak{n}$-preadic
topology $(0_{IV}, 19.6.4)$. All the conditions of application of `(22.7.5)` are therefore fulfilled.

**Remarks (22.7.7).**

<!-- label: 0_IV.22.7.7 -->

*(i) We shall later see, with Nagata, using `(22.7.6)`, that one can extend the conclusion of `(22.7.6)` to the case of
an arbitrary complete Noetherian local ring `(IV, 6.12.7)`.*

*(ii) The conclusion of theorem `(22.7.3)` is not necessarily exact when one no longer supposes that $[k : k^{p}]$ be
finite. Take for example $k = \mathbb{F}_{p}(X_{n})_{n \geq 0}$, $A = k[[T, U]]$, $\mathfrak{q}$ equal to the principal
ideal `A f`, where $f = U^{p} - \sum^{\infty}_{n=0} X_{n} T^{np}$; $A$ is a factorial ring in which $f$ is an extremal
element, for it is extremal in the polynomial ring `k((T))[U]`, hence also in the ring of formal series `k((T))[[U]]`
(Bourbaki, *Alg. comm.*, chap. VII, §3), and *a fortiori* in $A$. Take $\mathfrak{p} = \mathfrak{q}$, so that
$B_{\mathfrak{p}}$ is the field denoted $E$ in $(0_{IV}, 21.9.7)$, which is separable over $k$ (*loc. cit.*), hence a
$k$-algebra formally smooth. But one has here, with the notations of `(22.7.3)`, $k = K_{0} = K$, and the
$k$-derivations of $A$ into itself are the linear combinations of $\partial/\partial T$ and $\partial/\partial U$; since
one has $\partial f/\partial T = \partial f/\partial U = 0$, the criteria b) and b′) of `(22.7.3)` are not satisfied.*
