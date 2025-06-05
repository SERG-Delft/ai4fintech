---
layout: default
title: events
---

# Events

Within AFR, events are regularly organized, including a weekly team meeting at ING, as well as frequent meet-ups.

| When&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  Title           | Speaker           |
| --------------- | --------------- | ----------------- |
{% for event in site.data.events -%}
| {{event.date}}  | {%- if event.url %}[{{event.title}}]({{event.url}}){:target="_blank"}{%- else %}{{event.title}} {%- endif %}. {%- if event.slides %} [(Slides)]({{event.slides}}){:target="_blank"} {%- endif %} | {{event.speaker}} |
{% endfor  %}

<br/>

![](img/afr-launch-2019.jpeg)