import webbrowser, django , os
import locator, flags
from django.template import Template, Context
from django.conf import settings


settings.configure() # required by django
django.setup()

template = """
<html>
  <head>
    <title>Ip Locator</title>
    <link rel="stylesheet" type="text/css" href="main.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/3.0.3/normalize.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" media="screen" title="no title" charset="utf-8">
    <link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
  </head>
    <body style="font-family: 'Open Sans', sans-serif;">
      <div class="col-lg-4"></div>
      <div class="col-lg-4 col-md-12" style="position:absolute;top: 50%;left:50%;transform:translate(-50%, -50%);">
      <h1>{{full_name}}</h1>
      <center><img src= {{flag}} style="padding:20px"></center>
        <div class="panel panel-default">
          <div class="panel panel-heading">
            <div class="panel-title"><h2>Addressing information for: {{user_input}}</h2></div>
          </div>

          <div class="panel-body">
            <p class="Lead">IP address: {{ip}}</p>
            <p>Host name: {{hostname}}</p>
            <p>City: {{city}}</p>
            <p>Region: {{region}}</p>
            <p>Country: {{country}}</p>
            <p>Coordinates: {{loc}} </p>
            <p>Organization: {{org}}</p>
            <hr>
            <div><small>IP to location by Caleb Ellis and Elijah Ellis</small></div>
          </div>
        </div>
      </div>
    </body>
</html>
"""

def build(input_dict):


    region = input_dict['region']
    ip = input_dict['ip']
    hostname = input_dict['hostname']
    city = input_dict['city']
    country = input_dict['country']
    location = input_dict['loc']
    organization = input_dict['org']
    user_request_name = locator.user_input
    flag_file_name = flags.get_flag_image(country)
    country_full_name = flags.get_country_full_name(country)
    if country_full_name == None:
        country_full_name = "Couldn't retrieve Country name."


    t = Template(template)
    c = Context({"user_input":user_request_name,
    "region":region,
    "style":"main.css",
    "ip":ip,
    "hostname": hostname,
    "city":city,
    "country":country,
    "loc":location,
    "org":organization,
    "flag":flag_file_name,
    "full_name":country_full_name
    })

    tags = str(t.render(c)).splitlines()
    target = open("info.html", 'w')

    for i in range(0, len(tags)):
        target.write(tags[i])

    open_url("info.html")

def open_url(url):
    webbrowser.open_new(url)
