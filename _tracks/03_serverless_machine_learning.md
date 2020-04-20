---
layout: default
track-id: 3
title: Serverless Machine Learning
leader: Asterios Katsifodimos
---

# Track 3: Serverless Machine Learning

A typical machine learning pipeline consists of a sequence of data processing and model training steps, that need to be carefully orchestrated.
In this track, we will investigate the design of a Serverless model, corresponding to "Stateful Functions as a Service" (SFaaS) that execute various machine learning tasks. Thanks to this data scientists should be able to focus on building ML models and experiments, while the complexity of operationalizing  (e.g. scaling, high availability, security) is addressed by the underlying platform. ML models can be deployed to production without expert knowledge on the underlying infrastructure. The expectation is that this reduces time-to-market significantly. 

Research topics addressed include providing a data dependency graph by static analysis of data dependencies, as well as automated feature management in order to see if the dependency tree is fully resolved and as a result, it is safe to migrate to new features and delete the unnecessary and underutilized features.

Related work:

- Adil Akhter, Marios Fragkoulis, Asterios Katsifodimos: Stateful Functions as a Service in Action. PVLDB 12(12): 1890-1893 (2019)

- Andreas Kunft, Asterios Katsifodimos, Sebastian Schelter, Sebastian Breß, Tilmann Rabl, Volker Markl: An Intermediate Representation for Optimizing Machine Learning Pipelines. PVLDB 12(11): 1553-1567 (2019)

**Track leader:** Asterios Katsifodimos
