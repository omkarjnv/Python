<html>
{% load static %}
{% block content %}
<head>
    <!--Import Google Icon Font-->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <!--Import materialize.css-->
   <link type="text/css" rel="stylesheet" href="{% static 'css/materialize.min.css' %}" media="screen,projection" />
  <link type="text/css" rel="stylesheet" href="{% static 'css/main.css' %}" />
  <script defer src="https://use.fontawesome.com/releases/v5.0.6/js/all.js"></script>
  <!--Let browser know website is optimized for mobile-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />



    <title>Student Details</title>
</head>
<body>

<form action="" method="POST">
   {% csrf_token %}
    EID : <input type="text" name="eid" /><br/>
    name :  <input type="text" name="name" /><br/>

    Dept : <input type="text" name="dept" /><br/>
   Contact : <input type="text" name="contact" /><br/>


   <input type="submit" value="Proceed for Signup" />

</form>

</body>
{% endblock %}
</html>