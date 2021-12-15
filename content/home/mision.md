---
widget: blank
headless: true
weight: 30
active: true

title: 
subtitle: ""

height: 200px

gallery_item:
- album: mision
  image: 1.png
  caption: 1. Perform impactful research
- album: mision
  image: 2.png
  caption: 2. Optimize the world of FinTech
- album: mision
  image: 3.png
  caption: 3. Make innovation available to society

design:
    columns: "1"
    spacing:
        padding: ["0", "10vw", "0", "10vw"]
---
<div class="row">
  <div class="col-9">
    <div class="row">
      <h1>Our Mission</h1>
      {{<collage album="mision" resize_options="300x220" >}}
    </div>
    <div class="row">
      <h1>Partners</h1>
      {{<collage album="partners" resize_options="300x120" >}}
    </div>
  </div>


  
  <a class="twitter-timeline" data-width="300" data-height="700" href="https://twitter.com/Ai4Fintech?ref_src=twsrc%5Etfw">Tweets by Ai4Fintech</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>