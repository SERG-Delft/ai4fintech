---
layout: default
title: events
---

# Events

Within AFR, events are regularly organized, including a weekly team meeting at Cumulus Park, as well as frequent meet-ups.

| When&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  Title           | Speaker           |
| --------------- | --------------- | ----------------- |
{% for event in site.data.events -%}
| {{event.date}}  | {{event.title}}. {%- if event.slides %} [(Slides)]({{event.slides}}){:target="_blank"} {%- endif %} | {{event.speaker}} |
{% endfor  %}
