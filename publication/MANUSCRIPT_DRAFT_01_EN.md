# BYTE NDT Living Engineering: A Traceable Ultrasonic Digital-Twin Scenario from Blade Examination to Scanner Context

**Working manuscript — Draft 01 — 11 November 2026**
Authors proposed by the lead author: **Jean-Michel Puybouffat, Fabien Dedieu, Tumelo Machaha**.

Affiliations, corresponding author and contributor roles: to confirm with the coauthors.
Submission venue: to be selected. The four applications, including C2 scanner N2-R02, have been accepted in the lead author’s digital review. This is a working manuscript for joint review, not a submitted article.

## Abstract

Ultrasonic examination of turbine-blade roots combines constrained access, complex surface geometry and the need to relate encoded responses to a reproducible probe trajectory. This work presents BYTE NDT Living Engineering as a traceable workflow connecting examination data, mechanical registration, interactive replay and scanner design. Four complementary applications organise the demonstration: C1 examination without a mechanical scanner, C1 examination in its blade-and-scanner context, and the corresponding two levels for C2. C1 examines an extrados groove from the intrados side over 41 positions and 3,485 focal laws; C2 examines the first intrados groove from the extrados side over 199 positions and 16,915 focal laws. Original encoded responses, focal laws and reference tables remain identifiable when displayed on the mechanical geometry. The applications expose contact and target views, calculated coherent-sensitivity volumes, encoded cartography, indication analysis, TFM images, voxel views and reports. Scanner applications extend this chain with conformal shells, guided motion and a simulated encoder. Existing source tables report matches to five C1 and six C2 reference notches; these figures describe the source datasets rather than a new independent experiment. All four applications have been accepted in the lead author’s digital review. Workshop and virtual-reality activities form the next stage of development. The proposed contribution is a living-engineering approach in which object identity, models, examination evidence and operator context remain connected through traceable change. Physical scanner qualification and independent acoustic validation remain separate requirements.

**Keywords:** ultrasonic testing; turbine-blade root; phased array; digital twin; traceability; scanner design; encoded replay.

## 1. Introduction

Engineering knowledge about an inspected component is distributed across geometry, physical models, operating procedures, tooling and interpretation of results. These descriptions can remain individually useful while their relationships become difficult to inspect as the design evolves. This work addresses the continuity of those relationships through a concrete blade-root examination scenario.

We propose **living engineering** as a working concept: the representations, models, procedures, evidence and decisions associated with an engineering object remain connected and can evolve through documented technical and operational feedback. The research question is how to preserve the identity, assumptions and evidence of that object while moving between examination design, scanner context and workshop use. The definition is proposed for discussion; it is not asserted as an established standard.

The degree of data integration and the relationships between physical and virtual entities are important dimensions in published digital-twin classifications [1, 2]. The present contribution will be positioned against these dimensions using the connections actually implemented, rather than treating a 3D display as sufficient evidence of a twin. The current demonstrator establishes a coupled digital examination scenario on preserved data; workshop feedback and physical instrumentation are the next development stages.


For a blade-root examination, a useful representation must connect the position of the probe, the intended acoustic target and the results available to the operator. A cartography alone does not describe access between adjacent blades. A mechanical assembly alone does not establish which acquired response belongs to a particular pose. The purpose of the present work is to maintain this connection while moving from an examination representation to a scanner concept.

BYTE NDT Living Engineering organises this connection through four applications with explicit roles. The first level describes an examination on the blade geometry without the mechanical scanner. The second places the same examination in the assembly context, with the central blade, adjacent blades and scanner components. The two levels are implemented for two distinct examination configurations, C1 and C2. C1 provides the accepted reference for the presentation and operator interaction; C2 retains its own entry side, target, trajectory and acoustic data.

The term “living” refers here to a revisable engineering representation whose source versions and assumptions remain inspectable. The current demonstrators replay stored datasets. A live hardware connection, automated model updating or closed-loop control is not demonstrated. This distinction sets the scope of the digital-twin claim and the evidence that the article can support.

## 2. Examination cases and application structure

Both cases use the mechanical geometry of a blade root and its surroundings. The two examination directions are complementary rather than interchangeable. C1 places the PA on the intrados side and targets the first extrados groove. C2 places the PA on the extrados side and targets the first intrados groove, G1. The examination paths and data must therefore remain case-specific even when the interface and camera conventions are shared.

| Case | Entry → target side | Encoded positions | Elements | Focal laws | Source references |
|---|---|---:|---:|---:|---|
| C1 | Intrados → extrados groove | 41 | 8 × 8 | 3,485 | EDM_01–EDM_05 |
| C2 | Extrados → first intrados groove G1 | 199 | 8 × 8 | 16,915 | EDM_06–EDM_11 |

The law counts correspond to 85 laws per position. Exact probe specifications, excitation parameters, material properties and their provenance must be consolidated with the author's scientific annexes before submission.

The four application records, A1–A4, define the demonstrator set. A1 and A3 provide the examination-level representations. A2 and A4 connect these examinations to the scanner assemblies and operator controls. Acceptance of A1, A2 and A3 was recorded during the earlier review. The lead author subsequently accepted the C2 scanner application, A4 N2-R02, after reviewing the complete replay and the corrected display. This is acceptance of the digital demonstrator and its scenario.

### 2.1. Object identity and evidence lineage

The four applications share an engineering object and a traceable examination structure, while C1 and C2 retain their own acoustic configurations. This provides two independent distinctions: examination case and level of operational context. A scanner view must preserve its case’s contact path and results rather than borrowing the other case’s acoustic poses.

Historical and current evidence also remain distinct. According to the project provenance reviewed by the lead author, B001 is retained as a previously accepted historical digital-evidence layer for comparison and traceability. It is not substituted for the current B014 scenario; the current B014 detection is reconstructed from Fusion B009 data. The exact files and versions linking these layers will be documented before finalising the data-provenance section. This lineage statement must not be used to suggest that historical validation constitutes a new B014 experiment.

## 3. Data, coordinate systems and physical interpretation

### 3.1. Source preservation and mechanical registration

The workflow separates original examination responses from their placement in the mechanical scene. For each encoded pose, a rigid transformation maps an acoustic point to the mechanical frame:

**x_mechanical = R x_acoustic + t**, with **RᵀR = I** and **det R = +1**.

This transformation expresses a change of frame. It does not generate a new signal or alter an original amplitude. Points, direction vectors, surface normals and target coordinates must be treated consistently. Units and any scale conversion are applied once and retained in the provenance record.

The original virtual acoustic origin is distinguished from the surface contact point used to place the graphical or mechanical probe assembly. A continuous contact path supports the displayed motion between encoded positions, while the stored UT responses belong to the acquired positions. Interpolated motion must not imply that an intermediate response has been physically measured.

### 3.2. Display conventions

Complex geometry can obscure the probe or target. Section views and illustrative cutaways therefore serve different purposes. A local examination section is defined from contact and target geometry; a camera cutaway is a visibility convention. Neither should be mistaken for a deformation of the blade or a change to the acoustic reconstruction.

The C2 display history exposed this distinction: a nearly tangent section produced an apparently enlarged profile, while changing clipping planes could produce an apparent moving wall. The accepted examination-level presentation and the scanner review are now retained separately. In the scanner context view, the central geometry remains intact and the camera does not follow a moving cutaway. Adjacent-blade visibility and shell opacity support inspection of the assembly without changing component coordinates.

### 3.3. Calculated field and received data

The available 3D field represents calculated coherent sensitivity associated with the source laws. The interface uses a fixed gain reference for its dB display. This quantity is distinct from a measured pressure field, a complete backscattering solution and the amplitude units used in other cartographies. These quantities require separate legends and definitions in the final figures.

The theoretical annexes will state the assumptions governing mechanical-wave propagation, tensor transformations and ultrasonic excitation. Each theoretical relation must be mapped to an implemented module or identified as background or future work. General formulations involving Green functions, Kirchhoff, Born or diffraction theory cannot be claimed as implemented and validated merely because they provide relevant theory.

## 4. From examination replay to scanner context

The examination applications synchronise probe position, encoded signal, progressive cartography and displayed indications. The final views provide access to source analyses, TFM, voxel representations and reports. Provisional signal-derived candidates remain distinguishable from named reference EDM notches. A final reference match does not establish the absence of false positives.

The scanner applications add a mechanical layer to this examination workflow. The current concept uses two conformal shells, an integrated guidance slot, a moving assembly and a provisional water-supply route in the upper lip. Assembly and exploded views support explanation of component roles. Forward, reverse and stop controls operate on the registered path, while encoder counts are calculated from simulated travelled distance and a selectable resolution.

The accepted C2 level-2 application combines the accepted C2 examination payloads with the historical R02 scanner geometry. The two shells remain fixed in the mechanical frame; eight component meshes move with the C2 surface-contact frame. A separate application entry point prevents the review from replacing the accepted examination application. The geometry, registration, contact and field payloads are checked for identity before integration.

This architecture establishes a reviewable link between path and assembly, but it does not qualify the scanner hardware. The historical R02 clearance report used a coarse sampled field and reports a minimum sampled chariot clearance of approximately 0.116 mm. That number is neither a validated manufacturing allowance nor proof of continuous clearance against all surrounding blades. Full assembly interference, tolerances, clamping, water-film stability, actual probe mounting and actuation require their own evidence.

## 5. Available results and verification

The source validation tables report the following matches and position-error ranges. They are included to describe the available dataset, not as performance estimates for a newly manufactured scanner.

| Dataset | Matched reference notches | Position-error range in source table | Interpretation |
|---|---:|---:|---|
| C1 | 5/5 | 0.579–2.401 mm | Reference-table results from the original replay |
| C2 | 6/6 | 0–1.871 mm | Frozen source examination-table results |

Source: `C1_VALIDATION_REFERENCE.csv` at Scanner C1 R06 and `C2_VALIDATION_REFERENCE.csv` at Scanner C2 reference R06. C2 frozen examination-table maxima and outputs from the encoded-signal candidate detector are distinct source layers. The final article must explain their relationship before comparing detection or localisation metrics. A zero tabulated error is not evidence of zero physical uncertainty.

Software verification addresses a different question: whether an integration preserves the accepted inputs and presents them coherently. For the C2 scanner application, the recorded software evidence includes payload identity, registered mobile placement, rigid rotations, sampled beginning/intermediate/end poses, forward and reverse operation, stop behaviour, bilingual controls and access to final results. The reproducibility dossier includes browser reports, payload checks and selected images. The lead author completed the visual review after N2-R02. The software checks and this review remain distinct from an independent physical experiment.

No probability-of-detection estimate, experimental uncertainty budget or independent comparison with CIVA is established by the present material. Such claims require additional datasets and agreed comparison conditions.

## 6. Discussion: contribution and limits

The main contribution is a traceable connection between examination definition, data interpretation and scanner context. The four-application structure makes this connection explicit: a reviewer can inspect the examination without the mechanical scanner, then inspect the same case in its assembly context. Versioned sources permit a display correction to be distinguished from a change to the path or acoustic data.

Several limits constrain the conclusions. Visual acceptance of an application is not the same as mechanical qualification. Coherent sensitivity does not constitute a full received-pressure prediction. TFM and voxel image dimensions do not automatically equal physical flaw dimensions. Source notch matches do not establish general detection capability or false-positive performance. Finally, replayed data and a simulated encoder do not demonstrate physical acquisition or feedback control.

A technical review with an external specialist could help assess the assumptions, terminology and comparison design. The author has identified Fabrice Foucher / EXTENDE as a potential interlocutor in relation to CIVA. This is a proposed review route; no endorsement, collaboration or software equivalence is implied. A future comparison would require a shared geometry, material, excitation, focal laws, targets and quantitative outputs.

## 7. Workshop and virtual-reality development

The next activity announced by the lead author is workshop work with virtual reality. Its purpose is to bring the examination, assembly and interpretation scenario into an operator setting while preserving the coordinate systems and provenance of the four applications. Candidate tasks include identifying the central blade and target groove, examining an exploded scanner, returning to the assembled state, following the examination path and linking a selected position to its signal and reconstructed images.

The hardware, VR environment, imported geometries and interactions will be recorded when they are selected and used. Operator observations should be logged against a source version so that a change to the digital representation can be related to the observation that motivated it. This future feedback path is a concrete development of the living-engineering concept. No measured VR training benefit or physical closed-loop behaviour is claimed by the current demonstrators.

## 8. Conclusion and next stage

BYTE NDT Living Engineering provides a structured demonstrator connecting two ultrasonic examination cases to their scanner contexts while preserving identifiable source data. C1 supplies the accepted two-level reference, and C2 supplies an accepted complementary examination and scanner context. The four digital application versions are now identified in the dossier. The next step is to consolidate the scientific annexes and document the workshop and virtual-reality work with explicit links to the implemented models. The article can then support a precise account of the workflow and its current evidence, with physical qualification and independent acoustic validation treated as subsequent work.

## Data and software availability — draft

The four source records and commit identifiers are listed in the accompanying dossier. Before submission, record the exact deployed versions, dependencies, file checksums and launch instructions, and confirm redistribution rights for geometry, datasets and third-party components. Git commit identifiers provide traceability but do not replace a durable archived release for the final publication.

## Supplementary material — planned

- Annex A: mechanical-wave propagation, prepared by the author.
- Annex B: tensor calculus and coordinate construction of the twin, prepared by the author.
- Annex C: ultrasonic excitation and focal laws, prepared by the lead author.
- Annex D: FMC/TFM and voxel interpretation, with implementation-specific parameters to consolidate.
- Four application records with source manifests, browser evidence and operator instructions.

## References — initial verified selection

[1] Kritzinger, W., Karner, M., Traar, G., Henjes, J., Sihn, W. (2018). Digital Twin in manufacturing: A categorical literature review and classification. *IFAC-PapersOnLine*, 51(11), 1016–1022. https://doi.org/10.1016/j.ifacol.2018.08.474

[2] Jones, D., Snider, C., Nassehi, A., Yon, J., Hicks, B. (2020). Characterising the Digital Twin: A systematic literature review. *CIRP Journal of Manufacturing Science and Technology*, 29, 36–52. https://doi.org/10.1016/j.cirpj.2020.02.002

[3] Holmes, C., Drinkwater, B. W., Wilcox, P. D. (2005). Post-processing of the full matrix of ultrasonic transmit–receive array data for non-destructive evaluation. *NDT & E International*, 38(8), 701–711. https://doi.org/10.1016/j.ndteint.2005.04.002

The bibliography will be expanded with the lead author’s scientific annexes and a focused review of related engineering-twin work. Prague 2014 and Munich 2016 contributions require their original titles, coauthors and proceedings records before citation.

## Editorial items for the next author review

Confirm author names and order, affiliations, contributor roles and corresponding author; agree the definition and original contribution of living engineering; consolidate the B001/B009/B014 file-level provenance; verify the theoretical equations against the implemented modules; select publication figures from the frozen application versions; then choose the journal and adapt the manuscript to its requirements. No submission or external technical-review request has been sent.
