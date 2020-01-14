---
layout: default
title: Research Tracks
---

# Research Tracks

The AFR research tracks all lie at the intersection of Artificial Intelligence, Data Analytics, and Software Analytics in the context of FinTech.
Given this FinTech context, all tracks have three overarching themes in common:

1. **Human-centered**: AFR emphasizes artificial intelligence methods and techniques that in which humans are in the lead, from all stakeholder perspectives.
2. **Data-driven**: AFR recognizes that data and data management is key to AI-success, emphasizing data that is Findable, Accessible, Interoperable, and Reusable (FAIR).
3. **Software-defined**: AFR acknowledges that modern banking is software defined, seeking to leverage AI to advance its software development practices, and making these practices ready for the AI-based systems of the future.

These themes recur in each of the tracks, yet in different proportions, with some tracks having a strong focus on the software side, and others a stronger focus on the human side.


## Track 1: Software Analytics

The research area of software analytics seeks to leverage data collected from software engineering processes to improve the effectiveness and efficiency of these processes. Data collected for these purposes include issues, log data, source code repositories, epic descriptions, etc. Thanks to the abundance of data, it becomes increasingly viable to apply machine learning techniques (e.g., random forests, support vector machines, neural networks) to use historic development information to support current development activities.

In the ING context, this is particularly relevant for the over 600 squads involved in software development. A key concern is epic predictability, which will be addressed within this track. Another area of interest is dependency management, between squads, software libraries used, and in the context of larger software ecosystems.

The research methods used in this track will include statistical analysis of development (CDaaS) data, enriched with survey data collected from development teams. Outcomes will include prototype tools as well as guidelines on how to make the software development process itself data-driven.

Related work:

- Elvan Kula, Ayushi Rastogi, Hennie Huijgens, Arie van Deursen, Georgios Gousios: Releasing fast and slow: an exploratory case study at ING. ESEC/SIGSOFT FSE 2019: 785-795

- Hennie Huijgens, Ayushi Rastogi, Ernst Mulders, Georgios Gousios and Arie van Deursen. Analyze That! Rethinking Questions for Data Scientists in Software Engineering. Technical Report TUD-SERG-2019-003. Delft University of Technology, 2019.

- Hennie Huijgens, Davide Spadini, Dick Stevens, Niels Visser, Arie van Deursen: Software analytics in continuous delivery: a case study on success factors. ESEM 2018: 25:1-25:10


## Track 2: Data Integration

The data integration track recognizes the importance of data for almost any application of artificial intelligence at ING.
ING is a data-rich organization. Its data lake constitutes a federation of different data storage types. The relationships between the many different data sources evolve over time, and are hard to predict and manage.

The goal of this track is to use semantics-based data matching to recognize such data relationships automatically. In particular, machine learning will be applied for the purpose of meta-data matching, automated schema discovery, schema evolution, and schema alignment. The results can be used to support data engineers to make data integration decisions by means of dataset exploration, discovery, and integration recommendation.

The context in which this will take place is the ING cloud infra-service platform, which continuously collects operational data from a large range of private cloud services operated by ING across layers.

Related work:

- Hennie Huijgens, Eric Greuter, Jerry Brons, Evert A. van Doorn, Ioannis Papadopoulos, Francisco Morales Martinez, Mauricio Finavaro Aniche, Otto Visser, Arie van Deursen: Factors affecting cloud infra-service development lead times: a case study at ING. ICSE (SEIP) 2019: 233-242

- Daniel Vliegenthart, Sepideh Mesbah, Christoph Lofi, Akiko Aizawa, Alessandro Bozzon: Coner: A Collaborative Approach for Long-Tail Named Entity Recognition in Scientific Publications. TPDL 2019: 3-17


## Track 3: Serverless Machine Learning

A typical machine learning pipeline consists of a sequence of data processing and model training steps, that need to be carefully orchestrated.
In this track, we will investigate the design of a Serverless model, corresponding to "Stateful Functions as a Service" (SFaaS) that execute various machine learning tasks. Thanks to this data scientists should be able to focus on building ML models and experiments, while the complexity of operationalizing  (e.g. scaling, high availability, security) is addressed by the underlying platform. ML models can be deployed to production without expert knowledge on the underlying infrastructure. The expectation is that this reduces time-to-market significantly. 

Research topics addressed include providing a data dependency graph by static analysis of data dependencies, as well as automated feature management in order to see if the dependency tree is fully resolved and as a result, it is safe to migrate to new features and delete the unnecessary and underutilized features.

Related work:

- Adil Akhter, Marios Fragkoulis, Asterios Katsifodimos: Stateful Functions as a Service in Action. PVLDB 12(12): 1890-1893 (2019)

- Andreas Kunft, Asterios Katsifodimos, Sebastian Schelter, Sebastian Breß, Tilmann Rabl, Volker Markl: An Intermediate Representation for Optimizing Machine Learning Pipelines. PVLDB 12(11): 1553-1567 (2019)

## Track 4: Deploying ML Models at Scale

The deployment of ML-applications brings in a unique set of engineering challenges. In particular if models are re-trained and re-deployed frequently, full automation of all relevant deployment tasks is needed. This includes monitoring and optimization in production, as well as data quality validation. For models requiring explainability, verification of not just outputs but also of the revised explanations will be necessary.
In this track we will seek to address such challenges at ING scale.

Related work:

- Saleema Amershi, Andrew Begel, Christian Bird, Robert DeLine, Harald C. Gall, Ece Kamar, Nachiappan Nagappan, Besmira Nushi, Thomas Zimmermann:
Software engineering for machine learning: a case study. ICSE (SEIP) 2019: 291-300

- Jimmy Lin and Dmitriy Ryaboy. 2013. Scaling big data mining infrastructure: the Twitter experience. SIGKDD Explor. Newsl. 14, 2 (April 2013), 6-19.


## Track 5: Continuous Experimentation

Continuous experimentation for consumer facing software is the practice to roll out features in a controlled way, measuring their impact on key performance indicators as much as possible.
This track connects the end user behavior (as measured through interactions with the software) with the software development teams that make decisions about feature implementations, thus closing the value chain from developer to end user.

Topics of interest include A/A and A/B testing, optimal statistical procedures, feature and variability management, reducing experiment duration while keeping track of long term objectives, and the identification of overall evaluation criteria as well as guard rail metrics.
The resulting metrics and measurement platforms will facilitate (machine) learning as well as (simulated) search-based optimization of the overall platform.

Related work:

- Titus Barik, Robert DeLine, Steven M. Drucker, Danyel Fisher:
The bones of the system: a case study of logging and telemetry at Microsoft. ICSE (Companion Volume) 2016: 92-101

- Ron Kohavi, Roger Longbotham: Online Controlled Experiments and A/B Testing. Encyclopedia of Machine Learning and Data Mining 2017: 922-929

- Ernst Mulders, Kevin Anderson, Hennie Huijgens, Georgios Gousios, Lukas Vermeer, and Arie van Deursen. ABvalidator, the three A’s of A/B Test validation. Technical Report TUD-SERG-2019-xyz, 2019. Submitted.

- Mónica Marrero, Claudia Hauff: A/B Testing with APONE. SIGIR 2018: 1269-1272


## Track 6: AI-Based Quality, Testing, and Security

Over the past few years, the software engineering research community has booked substantial progress in reformulating many software engineering processes as _search-based problems_. 

In particular, _testing_ can be considered as a _search_ for a set of test _cases_ that together meet a given _adequacy_ criterion, such as line coverage.
The search can start from randomly generated test inputs. These can then be _combined_ in such ways that the chances of increasing the coverage become higher and higher. This, then, gives rise to the application of _evolutionary algorithms_ for the purpose of software testing.
A well known research tool that reflects the state of the art is `evosuite.org`, to which TU Delft has contributed as well.

In the context of AFR, search-based testing techniques offer unique opportunities to further advance automated testing approaches within ING.
In particular, in this track we seek to lift search-based test generation techniques from the unit to the integration and system test levels. Furthermore, we will explore how search-based techniques can be used for the purpose of _security_ testing, bringing more intelligence, for example, to the current state of the art in fuzzing and penetration testing.

Related work:

- Annibale Panichella, Fitsum Meshesha Kifetew, Paolo Tonella: Automated Test Case Generation as a Many-Objective Optimisation Problem with Dynamic Selection of the Targets. IEEE Trans. Software Eng. 44(2): 122-158 (2018)

- Sadeeq Jan, Annibale Panichella, Andrea Arcuri, Lionel C. Briand: Automatic Generation of Tests to Exploit XML Injection Vulnerabilities in Web Applications. IEEE Trans. Software Eng. 45(4): 335-362 (2019)

- Maria Kechagia, Xavier Devroey, Annibale Panichella, Georgios Gousios, Arie van Deursen: Effective and efficient API misuse detection via exception propagation and search-based testing. ISSTA 2019: 192-203


## Track 7: Interactive Agents and Intelligent Orchestration

A part of compliance and due diligence in preventing abuse and fraud is tracking and verifying evidence and compliance documents. This process is labor-intensive, time consuming and error-prone due to its mostly manual nature. While automation seems the solution to this problem pure automation based on machine learning creates the possibility for gaming the system due to the closed nature of such networks and the inherent vulnerability to adversarial machine learning.

We propose to create an co-active agent to aid in the verification of compliance by facilitating collaboration between a human and specific limited machine learning agents into a coherent and efficient working process. 

A first version could simply provide humans with assistance on knowledge about compliance and policy, while a following version could gradually include more and more supporting AI system like analysis of evidence using Natural Language Processing (NLP).

A final version could extend the support agent concept to the client side to advise employees about compliance and evidence before submitting documents to the central repository to create awareness and prevention training on the policies and the reasons behind them and at the same time improving quality of submissions, further improving efficiency of policy verification.

Related work:

- Gabriel Murray, Catharine Oertel: Predicting Group Performance in Task-Based Interaction. ICMI 2018: 14-20

- Vincent J. Koeman, Koen V. Hindriks, Catholijn M. Jonker: Automating failure detection in cognitive agent programs. IJAOSE 6(3/4): 275-308 (2018)


## Track 8: Natural Language Processing and Information Retrieval

RegTech is a subset of FinTech aimed at delivering regulatory requirements more efficiently and effectively than existing capabilities. This particularly relates to Know Your Customer (KYC) and Customer Due Diligence (CDD) requirements set in place to prevent banks from being used, intentionally or unintentionally, by criminal elements for money laundering activities.

Current advances in Natural Language Processing (NLP) open up new possibilities to strengthen KYC and CDD activities.
Written documents from regulators describe the constraints and requirements banks and their customers must adhere to.
The assessment of compliance is based on a series of data sources, which can be structured (stored in databases) or unstructured, in which case it is, again, written text.
The route that will be explored in the context of AFR is to use NLP to distill the requirements from regulatory documents automatically. With that in place, customer-related data, can be used to assess compliance. Here, again, for the unstructured parts, NLP techniques will be applied to distill elements that can be used for formal compliance evaluation.

One line of research in this track will focus on applying existing NLP techniques to the regulatory domain.
Furthermore, we anticipate that current NLP techniques may have to be adjusted to the regulatory domain.
Modern NLP techniques are largely statistical in nature, being trained on large bodies of existing text.
We anticipate that regulatory documents will have unique characteristics, requiring tailor-made NLP models.
ING's historic data of already conducted KYC and CDD assessments will provide the starting point for such tailor-made NLP models.

-  Arner, Douglas W. and Barberis, Janos Nathan and Buckley, Ross P., FinTech, RegTech and the Reconceptualization of Financial Regulation. Northwestern Journal of International Law & Business, 2017.

- Felipe Moraes, Kilian Grashoff, Claudia Hauff: On the impact of group size on collaborative search effectiveness. Inf. Retr. Journal 22(5): 476-498 (2019)


## Track 9: User Experience and Personalization

In order to be able to optimally serve its customers' needs and demands, ING seeks to offer personalized and relavant customer journeys, on its mobile as well as its web platforms.
The underlying system interactions can be short term (one web session) as well as long term, spanning years if not decades, in case of, e.g., mortgages or pensions.

Within this track we seek to develop novel methods and techniques in the areas of user modeling, adaptation, and personalization (UMAP), within the context of banking.
Topics of interest include intelligent orchestration, personalized recommender engines, steering user behavior, user preference elicitation, web user profiles, adaptive navigation support, semantic web technologies, and the personalized social web.

Related work:

- Kirsten A. Smith, Matt Dennis, Judith Masthoff, Nava Tintarev: A methodology for creating and validating psychological stories for conveying and measuring psychological traits. User Model. User-Adapt. Interact. 29(3): 573-618 (2019)

- Yucheng Jin, Nyi Nyi Htun, Nava Tintarev, Katrien Verbert: ContextPlay: Evaluating User Control for Context-Aware Music Recommendation. UMAP 2019: 294-302


## Track 10: Fairness-Aware Machine Learning

More and more software services in the banking domain rely on machine learning.
This makes it crucial that such services can be considered fair, and not influenced negatively by potential biases in the training data. Here, the banking domain introduces an additional, critical need for fairness, as the bank's algorithms affect customer's abilities to open a bank account, obtain a loan or mortgage, or buy a house.

This calls for machine learning and recommender system approaches that offer ways to quantify and mitigate algorithmic bias.
An open question at the moment is how fairness constraints can be expressed, and to what extent current approaches like stating desired statistical distributions of key attributes are sufficient.
Another question is how, given potentially biased ML results, subsequent ranking algorithms can be made aware of this bias so that it can adjust its ranks accordingly.
Lastly, fairness-aware machine learning calls for a clear ethical framework, which offers a well-defined for humans who are in control.

Related work:

- Sarah Bird, Ben Hutchinson, Krishnaram Kenthapadi, Emre Kiciman, Margaret Mitchell: Fairness-Aware Machine Learning: Practical Challenges and Lessons Learned. KDD 2019:3205-3206

- Sandy Manolios, Alan Hanjalic, Cynthia C. S. Liem: The influence of personal values on music taste: towards value-based music recommendations. RecSys 2019:501-505

- Nava Tintarev, Judith Masthoff: Explaining Recommendations: Design and Evaluation. Recommender Systems Handbook 2015:353-382