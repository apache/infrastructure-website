Title: Articles
Date: '2022-10-19T02:28:20+00:00'

{% block content %}

{% for article in articles %}
    <!-- Post -->
    <div class="title">
      <h2><a href="single.html">{{ article.title }}</a></h2>
      <!-- <p>{{ article.summary }}</p> -->
    </div>
{% endfor %}

{% endblock content %}
