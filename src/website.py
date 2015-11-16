import webbrowser
import locator
from django.template import Template, Context
from django.conf import settings
settings.configure() # required by django

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

    user_request_name = locator.user_input
    region = input_dict['region']
    ip = input_dict['ip']
    hostname = input_dict['hostname']
    city = input_dict['city']
    country = input_dict['country']
    location = input_dict['loc']
    organization = input_dict['org']


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
    })

    tags = str(t.render(c)).splitlines()

    target = open("info.html", 'w')

    for i in range(0, len(tags)):
        target.write(tags[i])

    open_url("info.html")


def open_url(url):
    webbrowser.open_new(url)
