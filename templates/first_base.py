<!DOCTYPE html>
<html lang="fr">
{% load staticfiles %}


  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="author" content="Henri E. Francois" />
    <title>PharmaOnline | Bienvenue </title>

    <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.css' %}" />
    <link rel="stylesheet" type="text/css" href="{% static 'css/freelancer.css' %}" />
    <link rel="stylesheet" type="text/css" href="{% static 'font-awesome/css/font-awesome.min.css' %}" />



    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

  </head>


  <body id="page-top" class="index">
    <nav class="navbar navbar-default navbar-fixed-to-top">
      <div class='container-fluid'>
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="{% url 'accueil' %}">
            <img alt="Brand" src="{% static "img/quick-pharma-logo.png" %}" height="120%" width="30px"/>
          </a>
        </div>

          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
              <!--<li><a href="#">Carte</a></li>-->
              <li><a href="{% url 'medicaments:liste-publique' %}">Medicaments</a></li>
              <li class="disabled"><a href="#">Carte</a></li>
            </ul>
            <form class="navbar-form navbar-left" role="search" method='GET' action="{% url 'haystack_search' %}">
              <div class="form-group">
                <input class="form-control" type="text" name='q' placeholder="Search">
              </div>
              <button type="submit" class="btn btn-danger"><span class="glyphicon glyphicon-search"></span></button>
            </form>
            <ul class="nav navbar-nav navbar-right">
              <!--li><a href="#">Link</a></li>-->
              {% if request.user.is_authenticated %}
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Mon Compte <span class="caret"></span></a>
                <ul class="dropdown-menu">
                  <li class="text-center"><a href="{% url 'medicaments:ajouter' %}">Ajouter des Medicaments</a></li>
                  <li class="text-center"><a href="{% url 'medicaments:inventaire' %}">Modifier les Medicaments</a></li>
                  <li role="separator" class="divider"></li>
                  <li class="text-center"><a href="https://medoc.herokuapp.com">Aller a MeDOC</a></li>
                  <li class="text-center"><a href="{% url 'accounts:logout' %}">Se deconnecter</a></li>
                </ul>
              </li>
              {% else %}
              <li><a href="{% url 'accounts:login' %}">Login</a></li>
              {% endif %}
            </ul>
          </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
      </nav>

      {% block content %}
      {% endblock %}

      <!-- Footer -->
      <footer class="footer">
        <div class="container">
          <p>Copyright &copy; PharmaOnline 2016</p>
      </footer>



      <div class="scroll-top page-scroll visible-xs visible-sm">
          <a class="btn btn-primary" href="#page-top">
              <i class="fa fa-chevron-up"></i>
          </a>
      </div>
  </body>


      <!-- jQuery -->
      <script src="{% static 'js/jquery.js' %}"></script>

      <!-- Bootstrap Core JavaScript -->
      <script src="{% static 'js/bootstrap.min.js' %}"></script>
