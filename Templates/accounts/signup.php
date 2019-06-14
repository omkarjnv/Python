<html>
{% load static %}
{% block content %}
<head><!--Import Google Icon Font-->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <!--Import materialize.css-->
  <link type="text/css" rel="stylesheet" href="{% static 'css/materialize.min.css' %}" media="screen,projection" />
  <link type="text/css" rel="stylesheet" href="{% static 'css/main.css' %}" />
  <script defer src="https://use.fontawesome.com/releases/v5.0.6/js/all.js"></script>
  <!--Let browser know website is optimized for mobile-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sign-Up</title>

  </head>

{%load crispy_forms_tags%}

<form action="" method="post" >
    {% csrf_token %}
{{ form|crispy}}

<input class="btn waves-effect" type="submit" value="Signup" />
</form>

{% endblock %}



</html>