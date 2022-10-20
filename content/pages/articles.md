Title: Articles
Date: '2022-10-19T02:28:20+00:00'

{% for article in articles %}
    <!-- Post -->
    <article class="post">
      <header>
        <div class="title">
          <h2><a href="single.html">{{ article.title }}</a></h2>
          <!-- <p>{{ article.summary }}</p> -->
        </div>
    </article>
{% endfor %}
