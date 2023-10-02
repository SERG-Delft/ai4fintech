---
layout: track
track-id: 6
title: Trustworthy AI
leader: Cynthia Liem
phd: Patrick Altmeyer
---

More and more software services in the banking domain rely on machine learning. This makes it crucial that the outcomes of the machine learning procedures in these services can be trusted. To be able to assess this, the [7 key requirements of the EU’s Ethics Guidelines for Trustworthy Artificial Intelligence](https://ec.europa.eu/futurium/en/ai-alliance-consultation) (Human agency and oversight; Technical Robustness and safety; Privacy and data governance; Transparency; Diversity, non-discrimination and fairness; Societal and environmental well-being; Accountability) will need concrete operationalization for the Fintech domain.

In several previous applications of machine learning (and statistical modeling), it has been found that concepts of ‘trust in’ and ‘correctness of’ models are not always clear-cut. Models that seem to perform well according to common performance metrics, may show unexpected behavior in the wild. Seemingly minor researcher degrees of freedom may have major outcomes on final results, and model outcomes may be misinterpreted, even by data scientists.

In this track, we approach trustworthy and explainable artificial intelligence from the perspective of _counterfactuals_: small perturbations to input values that lead to different model outcomes. Such counterfactuals can provide _recourse_, offering people means to strategically alter their behavior so that models do give desired outcomes.

## Selected Publications

- Patrick Altmeyer, Arie van Deursen, Cynthia C. S. Liem. Explaining Black-Box Models through Counterfactuals. JuliaCon Proceedings, 1(1), 130, 2023 ([preprint](https://doi.org/10.21105/jcon.00130)).

- Endogenous Macrodynamics in Algorithmic Recourse. P Altmeyer, G Angela, A Buszydlik, K Dobiczek, A van Deursen, Cynthia S. Liem. IEEE Conference on Secure and Trustworthy Machine Learning (SaTML), 418-431, 2023 ([preprint](https://openreview.net/pdf?id=-LFT2YicI9v))

- Cynthia C. S. Liem and Chris Mostert, “Can't Trust the Feeling? How Open Data Reveals Unexpected Behavior of High-level Music Descriptors,” in ISMIR 2020.

## Tool support

The track has resulted into a number of packages in Julia, available at [https://github.com/JuliaTrustworthyAI](https://github.com/JuliaTrustworthyAI).
