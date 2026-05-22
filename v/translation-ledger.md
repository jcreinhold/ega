# Translation ledger — EGA V

Running Blass→idiomatic-English term ledger for the EGA V polish. Unlike EGA I-IV (which are translated from French
OCR), the Blass & Blass source is already in English; this ledger records the few terms whose Blass rendering needed
modernization, French residue retired, or notational standardization.

Extends $docs/books/ega/iv/translation-ledger.md$ verbatim. Most vocabulary inherits unchanged from EGA IV.

## Inherited from EGA IV

The EGA IV ledger transfers without modification. In particular: `préschéma` → prescheme, `schéma` → scheme, the
differential and formal-smoothness vocabulary $(\Omega_{B/A}, \operatorname{Der}, F, p-basis, \Upsilon, \cdots)$, the
depth and regularity machinery `(prof, coprof, dim, codim, Cohen-Macaulay, …)`, the regular-immersion and divisor
vocabulary `(immersion régulière, immersion transversalement régulière, 𝓜_X, 𝓜_X^×, Pic(X), …)`, the étale-morphisms
vocabulary, the cohomology and spectral-sequence vocabulary, and the citation forms for $(M, \cdots)$, $(G, \cdots)$,
$(T, \cdots)$, $(FAC, \cdots)$, `(Bourbaki, Alg. comm., …)`, $(Nagata, \cdots)$, $(Zariski-Samuel, \cdots)$.

The Bourbaki, Mumford, and Seidenberg references introduced in §V.5 and §V.6 are recorded below.

## §V.1 — Singular and supersingular zeros (Blass prenote, formerly EGA IV §16)

| Blass / OCR                                           | Idiomatic English                             | Reference | Note                                                                  |
| ----------------------------------------------------- | --------------------------------------------- | --------- | --------------------------------------------------------------------- |
| singular zero (or root) of $\phi$                     | singular zero of $\phi$                       | V.1.1     | "root" dropped; "zero" alone is unambiguous in scheme theory.         |
| supersingular zero                                    | supersingular zero                            | V.1.1     | Term preserved.                                                       |
| ordinary singular zero                                | ordinary singular zero                        | V.1.1     | Used as the contrast to "supersingular".                              |
| non-singular zero                                     | non-singular zero                             | V.1.2     | Equivalent to "smooth zero" / "regular zero of $V(\phi)$".            |
| geometrically singular zero of $\phi$ relative to $k$ | geometrically singular zero (relative to $k$) | V.1.3     | The "relative to $k$" qualifier preserved.                            |
| geometrically supersingular zero                      | geometrically supersingular zero              | V.1.3     |                                                                       |
| $V (\phi)sing$                                        | $V(\phi)_{sing}$                              | V.1.5     | The closed-set notation.                                              |
| $V (\phi)\sup sing$                                   | $V(\phi)_{supsing}$                           | V.1.7     | Or $V(\phi)_{\sup sing}$ if disambiguation is needed.                 |
| $d0\phi$, $d1\phi$, $d2\phi$                          | $d^{0}\phi$, $d^{1}\phi$, $d^{2}\phi$         | V.1.5     | Unicode superscripts; matches EGA IV §0_IV.20.                        |
| principal parts of order 1                            | principal parts of order 1                    | V.1       | Inherited from EGA IV §0_IV.20.                                       |
| $PX/Y2$                                               | $\mathcal{P}^{2}_{X/Y}$                       | V.1.5     | Script 𝒫 for principal-part bundle; matches EGA IV.                   |
| $gr1 (PX/Y1)$                                         | $gr^{1}(\mathcal{P}^{1}_{X/Y})$               | V.1.5     |                                                                       |
| $M (\phi)$                                            | $M(\phi)$                                     | V.1.5     | Quadratic form on the cotangent space.                                |
| $D(\phi)$                                             | $D(\phi)$                                     | V.1.5     | Determinant of $M(\phi)$.                                             |
| sub-prescheme of zeros of $\psi$                      | subprescheme of zeros of $\psi$               | V.1.5     | Hyphenation modernized (no hyphen in "subprescheme"; matches EGA II). |
| $Ram(V'/Y)$                                           | $Ram(V'/Y)$                                   | V.1.7     | Ramification subprescheme.                                            |
| `en termes de papa` (Fr)                              | "in the old language"                         | V.1.7     | First occurrence: translator footnote quotes the French verbatim.     |
| `sous-entendu` (Fr)                                   | "tacitly assumed", "understood"               | V.1.5     | Used to mark which auxiliary scheme is implicit.                      |
| `confondus` (Fr)                                      | "coinciding"                                  | V.1.7     | Used in describing "infinitely near singular points" picture.         |

## §V.2 supplements — §§V.2.15-2.16 (formerly EGA IV §§17.15-17.16)

| Blass / OCR                | Idiomatic English          | Reference | Note                                            |
| -------------------------- | -------------------------- | --------- | ----------------------------------------------- |
| Jacobian criterion         | Jacobian criterion         | V.2.15    | Reference to §0_IV.22.6 and §IV.17.             |
| regular at a point         | regular at a point         | V.2.15    | Inherited from §0_IV.17.                        |
| critical point (of $\phi$) | critical point (of $\phi$) | V.2.15    | Synonym for "singular zero" in the smooth case. |
| $\Omega^{1}_{X/k}$ ($x$)   | $\Omega^{1}_{X/k}(x)$      | V.2.15    | Stalk-at-$x$ notation.                          |

## §V.5 — Hyperplane sections and conic projections (formerly EGA IV §20)

| Blass / OCR                                | Idiomatic English                          | Reference | Note                                                                        |
| ------------------------------------------ | ------------------------------------------ | --------- | --------------------------------------------------------------------------- |
| hyperplane section                         | hyperplane section                         | V.5.1     |                                                                             |
| generic hyperplane section                 | generic hyperplane section                 | V.5.2     |                                                                             |
| conic projection                           | conic projection                           | V.5.9     | The projection from a sub-linear-space.                                     |
| Bertini-Zariski theorem                    | Bertini-Zariski theorem                    | V.5.3     | Inherited terminology; both names retained.                                 |
| Seidenberg-style theorem                   | Seidenberg-style theorem                   | V.5.6     | Connectedness/irreducibility of generic sections.                           |
| linear system                              | linear system                              | V.5.16    | Subscheme-of-`Hilb`/`Pic` interpretation in §V.5.16.                        |
| projective bundle, projective fibration    | projective bundle, projective fibration    | V.5.1     | Both terms used; "fibration" emphasises the morphism structure.             |
| Grassmannian                               | Grassmannian                               | V.5.10    | $Grass_{k}(V)$ or $G(k, n)$; preserve EGA-style.                            |
| $\Lambda$, $\Pi$                           | $\Lambda$, $\Pi$                           | V.5       | Greek capitals for linear subspaces of $\mathbb{P}$.                        |
| $\mathbb{P}^{n}_{X}$, $\mathbb{P}^{n}_{S}$ | $\mathbb{P}^{n}_{X}$, $\mathbb{P}^{n}_{S}$ | V.5.1     | Relative projective space.                                                  |
| $p\hat{e}le m\hat{e}le$ (Fr)               | "pell-mell", or restructure                | V.5.1     | Used in Grothendieck's commentary; translator footnote at first occurrence. |

## §V.6 — Invertible sheaves and divisors; linear systems (formerly EGA IV §21)

| Blass / OCR                            | Idiomatic English                               | Reference | Note                              |
| -------------------------------------- | ----------------------------------------------- | --------- | --------------------------------- |
| relative divisor                       | relative divisor                                | V.6.2     |                                   |
| relative effective Cartier divisor     | relative effective Cartier divisor              | V.6.2     | Term locked.                      |
| Picard group of a projective fibration | Picard group of a projective fibration          | V.6.1     |                                   |
| $\operatorname{Pic}(X/S)$              | $\operatorname{Pic}(X/S)$                       | V.6.1     | Relative Picard functor / scheme. |
| invertible sheaf                       | invertible sheaf                                | V.6.1     | Inherited from EGA II/III/IV.     |
| linear system of divisors              | linear system of divisors                       | V.6.5     | Relative version.                 |
| $O(1)$, $\mathcal{O}_{\mathbb{P}}(1)$  | $\mathcal{O}(1)$, $\mathcal{O}_{\mathbb{P}}(1)$ | V.6.1     | Standard EGA II form.             |
| multiprojective fibration              | multiprojective fibration                       | V.6.2     |                                   |

## Standing abbreviations introduced in EGA V

| Key                           | Work                                                                                                                              |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| $(Mumford, \cdots)$           | D. Mumford, _Lectures on curves on an algebraic surface_ (Princeton Math. Notes, 1966).                                           |
| $(Vaiello, \cdots)$           | Used in source-trace footers only; the Vaiello unified edition is a reconciliation reference, not a citable work in prose.        |
| $(Bourbaki S\acute{e}m. 232)$ | A. Grothendieck, _Techniques de construction en géométrie analytique_ (Sém. Bourbaki, exposé 232, 1961-62).                       |
| $(Bourbaki S\acute{e}m. 236)$ | A. Grothendieck, _Techniques de descente et théorèmes d'existence en géométrie algébrique_ (Sém. Bourbaki, exposé 236, 1959-60+). |
| $(Bourbaki S\acute{e}m. 261)$ | A. Grothendieck, _Techniques de construction de schémas_ (Sém. Bourbaki, exposé 261, 1960-61).                                    |

These extend the EGA IV standing-abbreviation table. The full bibliographic entries appear in
[bibliography.md](bibliography.md).
