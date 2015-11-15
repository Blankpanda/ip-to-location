from django.template import Template, Context
from django.conf import settings
settings.configure() # required by django


template = """
<html>
<head>
<title>{{region}}</title>
<link rel="stylesheet" type="text/css" href="{{style}}">

</head>
<body>
<div class="top">
 IP to location by Caleb Ellis
<div/>
<h1>IP address: {{ip}} </h1>
<p> {{hostname}} </p>
<p> {{city}} </p>
<p> {{region}} </p>
<p> {{country}} </p>
<p> {{loc}} </p>
<p> {{org}} </p>
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


    t = Template(template)
    c = Context({"region":region,
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
