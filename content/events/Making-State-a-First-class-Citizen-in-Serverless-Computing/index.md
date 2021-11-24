---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Making State a First Class Citizen in Serverless Computing"
event:
event_url:
location: ING Analytics & Modelling Community Event
address:
  street:
  city:
  region:
  postcode:
  country:
summary: In the serverless model, users upload application code to a cloud platform and the cloud provider undertakes the deployment, execution and scaling of the application, relieving users from all operational aspects. Although very popular, current serverless offerings offer poor support for the management of local application state, the main reason being that managing state and keeping it consistent at large scale is very challenging. As a result, the serverless model is inadequate for executing stateful, latency-sensitive applications. In this talk we will present Rho, a high-level programming model for developing stateful functions and deploying them in the cloud. Our programming model allows functions to retain state as well as call other functions. In order to deploy stateful functions in a cloud infrastructure, we translate functions and their data exchanges into a stateful dataflow graph. We will then demonstrate that using existing open-source dataflow engines (Apache Flink, and others) as a runtime for stateful functions, we can deploy scalable and stateful services in the cloud with surprisingly low latency and high throughput.

abstract: Few sentecnes about the event. Few sentecnes about the event. Few sentecnes about the event. Few sentecnes about the event. Few sentecnes about the event.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2021-11-25T07:55:33+01:00
date_end: 2021-11-26T07:55:33+01:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2021-11-24T07:55:33+01:00

authors: [Adil Akhter, Asterios Katsifodimos]
tags: []

# Is this a featured event? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your event's folder or a URL.
url_slides:

url_code:
url_pdf:
url_video:

# Slides
# Contain the path from content
slides: "/slides/test.pdf"

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
