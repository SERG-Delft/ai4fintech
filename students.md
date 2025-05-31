---
layout: default
title: Student projects
---

# Student projects

We generally have positions available for TU Delft bachelor and master students in computer science.
These positions will be as intern at ING, supervised by researchers from AFR.
This can be part of the

- 2nd year TU Delft bachelor software project (in teams of 4)
- 3d year TU Delft bachelor thesis project (individual)
- TU Delft master thesis project (individual)

If you are interested in such a position, checkout the current [tracks](tracks.html) and contact the relevant [people](people.html). You will be hired as ING intern during your project, which includes an ING selection procedure. Be sure to contact us at least two months before the intended starting date of your project.
For all projects, it is required to spend at least 4 days per week at the ING CumulusPark campus.

If you study at a different university and you would like to write a research master thesis in the context of one of the AFR tracks, you should ask your university supervisor to contact us. We have limited places available, but are always interested in new research opportunities.

For general inquiries, please contact [Arie van Deursen].


<!--

## Current students

Name | Period | Role | Topic | Advisors
--|--|--|--|--
{% for student in site.data.students -%}
{%- unless student.status contains "Graduated" or student.status contains "Finished" or student.level == "PhD" or student.status == "" -%}
{{student.name}}     | {{student.status}} | {{student.level}} | {{student.topic}} | {{student.supervision}}
{% endunless -%}
{%- endfor %}

-->

<br/>

## Completed research projects

Name | Period | Role | Thesis       | Advisors
-----|--------|------|--------------|----------
{% for student in site.data.students -%}
{%- if student.status contains "Graduated" or student.status contains "Finished" -%}
{{student.name}}     | {{student.status}} | {{student.level}} | [{{student.topic}}]({{student.link}}) | {{student.supervision}}
{% endif -%}
{%- endfor %}




[Luís Cruz]: https://luiscruz.github.io
[Arie van Deursen]: https://avandeursen.com/about
