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

These themes recur in each of the tracks, yet in different proportions, with some tracks having a strong focus on the software side, and others a stronger focus on the data human side.

The AFR tracks are listed in the table.

| Id | Track  | PhD Candidate | Track leads |
|-|--------|---------------|----| 
{% for track in site.tracks -%}
{%- unless track.inactive -%}
| {{track.track-id}} | [{{track.title}}]({{track.url | relative_url}}) | {{track.phd}} | {{track.leader}} |
{%- endunless %}
{% endfor %}

<br/>