# XSS Demo

1. Execute `docker-compose up` in the root of this repository.
2. Visit [`localhost`](http://localhost/) in your browser.
3. Add a comment at the bottom of the page and include HTML-elements like


<script>
  alert('Hello World!');
</script>
Once the comment was added, the included HTML-snippet will be executed every time the page loads.


<script>
  alert(document.cookie);
</script>


