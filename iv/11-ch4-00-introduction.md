# Chapter IV — Local study of schemes and morphisms of schemes

<!-- original page 222 -->

## Sommaire

- **§1.** Relative finiteness conditions. Constructible sets in preschemes.
- **§2.** Base change and flatness.
- **§3.** Associated prime cycles and primary decompositions.
- **§4.** Base field change in preschemes.
- **§5.** Dimension and depth in preschemes.
- **§6.** Flat morphisms of locally Noetherian preschemes.
- **§7.** Application to the relations between a Noetherian local ring and its completion. Excellent rings.
- **§8.** Projective limits of preschemes.
- **§9.** Constructible properties.
- **§10.** Jacobson preschemes.
- **§11.**[^1] Topological properties of flat morphisms of finite presentation. Local criteria of flatness.
- **§12.** Study of the fibres of flat morphisms of finite presentation.
- **§13.** Equidimensional morphisms.
- **§14.** Universally open morphisms.
- **§15.** Study of the fibres of a universally open morphism.
- **§16.** Differential invariants. Differentially smooth morphisms.
- **§17.** Smooth, unramified, étale morphisms.
- **§18.** Complements on étale morphisms. Henselian local rings.
- **§19.** Regular and transversally regular immersions.
- **§20.** Hyperplane sections; generic projections.
- **§21.** Infinitesimal extensions.

> _Translator's note._ The sommaire above reproduces the 1964 announcement printed in Part 1. As the footnote warned,
> the program was revised during the later parts. **§11 was never published** — Part 3 (1966) prints §§8, 9, 10, 12, 13,
> 14, 15, skipping §11. **§§20 and 21 were redrawn**: in Part 4 (1967) §20 became *Meromorphic functions; pseudo-
> morphisms* and §21 became *Divisors*, replacing the announced "hyperplane sections" and "infinitesimal extensions"
> respectively. The translation files use the *published* §20 and §21 titles, and there is no §11 file.

<!-- original page 223 -->

The subjects treated in this chapter call for the following remarks.

**a)** Their common character is to bear on *local properties* of preschemes or of morphisms, i.e. properties considered
at a point, or at the points of a fibre, or in a neighbourhood (unspecified) of a point or of a fibre. These properties
are generally *topological*, *differential*, or *dimensional* in nature (i.e. they bring into play the notions of
dimension and depth), and they are tied to the properties of the local rings at the points in question. A typical
problem is to relate, for a given morphism `f : X → Y` and a point `x ∈ X`, the properties of `X` at `x` to those of `Y`
at `y = f(x)` and of the fibre `X_y = f⁻¹(y)` at `x`. Another is to determine the topological nature (for example,
constructibility, or being open or closed) of the set of points `x ∈ X` at which `X` has a given property, or for which
the fibre `X_y` through `x` has a given property at `x`. Similarly, one is interested in the topological nature of the
set of points `y ∈ Y` such that `X` has a given property at every point of the fibre `X_y`, or such that this fibre has
a given property.

**b)** The notions of greatest importance for the chapters that follow are those of *flat morphism of finite
presentation* and of *smooth morphism* and *étale morphism* (which are special cases of the former). Their detailed
study (together with that of related questions) really begins at §11.

**c)** §§1 through 10 may be regarded as preliminary in nature; they develop three types of technique, used not only in
the other sections of the chapter but, naturally, in the chapters that follow as well.

**`c_1`)** In §§1 through 4 we consider various aspects of the notion of *base change*, especially in relation with
finiteness or flatness conditions; we initiate, at its most elementary level, the technique of *descent* (the
"effectiveness" questions tied to that technique will be studied in Chapter V).

**`c_2`)** §§5 through 7 are centred on what we may call *Noetherian techniques*: the preschemes considered are always
supposed locally Noetherian, while no finiteness conditions are imposed on the morphisms; this is essentially because
the notions of dimension and depth are not really workable except for Noetherian local rings. Let us recall that §7
constitutes a "fine" theory of Noetherian local rings, used relatively little in the rest of the chapter.

**`c_3`)** §§8 through 10 provide, among other things, the means to *eliminate the Noetherian hypotheses* on the
preschemes under study, replacing them by suitable finiteness hypotheses ("finite presentation") on the morphisms
considered: the advantage of this substitution is that the latter hypotheses are stable under base change, which is not
the case for Noetherian hypotheses on preschemes.

<!-- original page 224 -->

The technique permitting this passage rests, on the one hand, on the use of the notion of *projective limit of
preschemes*, by means of which one may reduce a question to the same question under Noetherian hypotheses; on the other
hand, on the systematic use of constructible sets, which have the double advantage of being preserved under inverse
image (by an arbitrary morphism) and under direct image (by a morphism of finite presentation), and of having manageable
topological properties in locally Noetherian preschemes. The same techniques often allow further reduction to more
particular Noetherian rings, for example finitely generated `k`-algebras (`k` a field), and this is where the properties
of "excellent" rings (studied in §7) play a decisive role. Independently of the question of eliminating Noetherian
hypotheses, the techniques of §§8 through 10, of very elementary nature, are in constant use in almost all applications.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/11-chapter-iv-banner.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-1.pdf, pp. 222–224 -->

[^1]: The order and content of §§11 through 21 are given for information only and may be modified before publication.
