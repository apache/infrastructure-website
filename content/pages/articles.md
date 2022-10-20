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
        <!-- 
            <div class="meta">
              <time class="published" datetime="{{ article.date | strftime('%Y-%m-%d') }}">{{ article.date | strftime('%b %-d, %Y') }}</time>
              <a href="#" class="author"><span class="name">{{ article.author }}</span><img src="{{ SITEURL }}/theme/images/avatar.jpg" alt="" /></a>
            </div>
          </header>
          <a href="single.html" class="image featured"><img src="{{ SITEURL }}/theme/images/pic01.jpg" alt="" /></a>
          {{ article.content }}
          <footer>
            <ul class="actions">
              <li><a href="single.html" class="button large">Continue Reading</a></li>
            </ul>
            <ul class="stats">
              {% for tag in article.tags %}
              <li><a href="#">{{ tag.name }}</a></li>
              {% endfor %}
            </ul>
          </footer>
        -->
    </article>
{% endfor %}
