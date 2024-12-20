---
layout: default
title: Publications
---

# Publications

All publications of the AI for Fintech Research are available in (green) open access, mostly via the [TU Delft repository][pure].

[pure]: https://research.tudelft.nl/en/searchAll/index/?search=ai4fintech

## Key Publications

{% for publication in site.data.publications %}

1. {{publication.title}}.
  {%- if publication.author %}
  {{publication.author}}.
  {%- elsif  publication.authors -%}
    {%- for author in publication.authors %}
      {{author}}{% if forloop.last %}.{% else %},{% endif %}
    {%- endfor -%}
  {%- endif -%}
  {% if publication.venue %}
    {{publication.venue}},
  {%- endif %}
    {{publication.year}}.
  {%- if publication.journal %}
    {{publication.journal}}.
  {%- endif -%}
  {%- if publication.award %}
    🏆 {{publication.award}}.
  {%- endif -%}
  {%- if publication.preprint %}
    [Preprint]({{publication.preprint}}).
  {%- endif -%}
  {%- if publication.doi %}
    [DOI:&nbsp;{{publication.doi}}](https://doi.org/{{publication.doi}}).
  {%- endif -%}
  {%- if publication.arxiv %}
    [Arxiv preprint]({{publication.arxiv}}).
  {%- endif -%}
  {%- if publication.source %}
    [Source code]({{publication.source}}).
  {%- endif -%}
  {%- if publication.dataset %}
    [Dataset]({{publication.dataset}}).
  {%- endif -%}
  {%- if publication.slides %}
    [Slides]({{publication.slides}}).
  {%- endif -%}
  {%- if publication.video %}
    [Video]({{publication.video}}).
  {%- endif -%}
  {%- if publication.thesis %}
    [Link to thesis]({{publication.thesis}}).
  {%- endif -%}
{% endfor %}



<!--
## Publication List

<div id="publicationlist"></div>

<script language="javascript">

  var purexml_SERG = "https://purexml.ewi.tudelft.nl/convert/tu/research-id/ai4fintech";
  var page_nr = location.search;

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("publicationlist").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", purexml_SERG + page_nr, true);
  xhttp.send();
</script>

-->
