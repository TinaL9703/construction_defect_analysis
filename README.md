# construction_defect_analysis

Purpose: This repository relates to our Capstone Data Science Project, where our team uses for code version control and collaboration.

### Phase 1 - Data Extraction
This phase consists primarily of converting court case data into text format for further processing. Actions include:
1. Case information - date, case duration, parties involved (PII masking maybe, or identify builder with questionable conduct), unique case identifier, judge, legal representatives?
2. Case evidence - plaintiff and defendent claims, damages incurred
3. Case outcome - monetary outcomes, which party's claims to be dismissed
4. Cited cases - external case citation, renaming of to match citation for ease of case lookups

As part of this phase, some NLP language model might be necessary to prepare for data analysis:
- NER: Name entity resolution on large text
- Event extraction: similar to NER but with different tags
- Summarisation/topic modelling: simplify claims of the parties to broader categories for analysis

Research requirements:
- PDF parsers, language models to use, information extraction methodologies

### Phase 2 - Data Analysis
This phase aims to deepdive into the data extracted from Phase 1 and seeks to add any further text preprocessing if deemed necessary. Analysis can encompass:
1. Breakdown of claims/evidence type from builder and customer perspectives
2. Categorisation of outcomes
3. Correlation between case duration, judge involved and case outcomes
4. Examination of primary case's connection with cited case

### Phase 3 - Outcome Modelling
This phase seeks to implement a suitable ML method to tackle the prediction of case outcome via training on the 500 odd cases. Models being considered and their reasoning are:
1. NLP based model such as BERT: BERT is currently a state-of-the-art pretrained language model that can be easily adapted to this use case.
2. TBD

### Phase 4 - Simple Front-end UI (if time permits)

## Background - Construction industry
- High value: generates ~150 billion in value, which is about 9% of Australia's GDP.
- Outdated technology: no centralised platform to handle contracts, disputes and payments; no standardised contract templates across companies.
- Cashflow issues: Missed or late payments are frequent (prevalent in about a third of construction companies) and threat to people's livelihoods, sometimes resulting in bankrupcies.
