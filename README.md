# construction_defect_analysis

Purpose: This repository relates to our Capstone Data Science Project, where our team will use for code version control and collaboration.

## Phase 1 - Data Extraction
This phase consists primarily for the extraction of court case data into text format for further processing. Actions include:
1. Case information - date, case duration, parties involved (maybe part of PII to mask just as plaintiff vs defendent), unique case identifier, judge?
2. Case evidence - plaintiff and defendent claims, damages incurred
3. Case outcome - monetary outcomes, which party's claims to be dismissed
4. Cited cases - external case references

As part of this phase, some NLP language model might be necessary to assist with data analysis:
- NER: Name entity resolution on large text
- Event extraction: similar to NER but with different tags
- Summarisation/topic modelling: simplify claims of the parties to broader categories for analysis

## Phase 2 - Data Analysis
This phase aims to deepdive into the data extracted from above process and seeks to add any further text preprocessing if deemed required. Analysis can encompass:
1. Breakdown of claims/evidence type from builder and customer perspectives
2. Categorisation of outcomes
3. Correlation between case duration, judge involved and case outcomes
4. Examination of primary case's connection with cited case

## Phase 3 - Outcome Modelling
This phase will implement a suitable ML method to tackle the prediction of case outcome based on some % of the 500 cases. Models being considered and the reasoning are:
1. NLP based model such as BERT: BERT is currently a state-of-the-art pretrained language model that can be easily adapted to this use case.
2. TBD

## Phase 4 - Simple Front-end UI (if time permits)
