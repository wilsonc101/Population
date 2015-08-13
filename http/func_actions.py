from datetime import datetime
import json

import pymongo

import sys

import pygal
#from pygal.style import LightStyle
from pygal.style import CleanStyle


MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "population"


def postData(path, headers, payload):
    request_time = datetime.utcnow()

    required_fields = ['vehicle_id', 'vehicle_data']

    # Validate payload
    try:
        json_data = json.loads(payload)

        for field in required_fields:
            if field not in json_data: return(500, "Error: Payload invalid, missing " + field)        

    except:
        return(500, "Error: Payload failed JSON parsing")

    try:
        vehicle_collection = _mongo_db[json_data['vehicle_id']]
        vehicle_collection.insert({"timestamp":request_time, "vehicle_data": json_data['vehicle_data']})
        return(200, "OK")
    except:
        return(500, "Error: Failed to add vehicle data")


def getPopulation(query=None, handler=None):
    # Get params from query string
    if query != None:
        params = query.split("?")
        for param in params:
            if "=" in param: 
                key, value = param.split("=")
                if key == "population_id": population_id = value
    else:
        return(500, "Error: Missing query string")
    

    # HTML Start Header
    html_head_start = "<!DOCTYPE html>\n\
<html>\n\
  <head>\n\
   <script type=\"text/javascript\" src=\"http://kozea.github.com/pygal.js/javascripts/svg.jquery.js\"></script>\n\
   <script type=\"text/javascript\" src=\"http://kozea.github.com/pygal.js/javascripts/pygal-tooltips.js\"></script>\n"


    # HTML End Header 
    html_head_end = "</head>\n"

    #HTML Body
    html_body_start ="  <body>\n"

    html_body_end = "  </body>\n\
</html>"


    if True:
#    try:
        # Adjust formats
        xaxis_labels = []
        population_count = ['total_pop']
        imported_population_count = ['imported_pop']

        # Query collection and print
        population_data = _mongo_db[population_id].find()
    
        for entry in population_data:
            # Populate local arrys with other population data
            xaxis_labels.append(str(entry['iteration']))
            population_count.append(entry['living_population'])
            imported_population_count.append(entry['living_imported_population'])

        # Generate graphs
        population_count_graph = _createChart([population_count, imported_population_count], xaxis_labels)
        population_count_graph = "<br>\n<br>\n" + population_count_graph + "\n<br>"

        # Build response
        response = html_head_start + html_head_end + html_body_start + population_count_graph + html_body_end
        return(200, str(response))

#    except TypeError as e:
#        print e + "HERE"
#    except NameError as e:
#        print e + "HERE 22"

#    except:
#        print str(sys.exc_info()[0])
#        return(500, "Error: Failed to generate response ")




def _createChart(data_lists, labels):
    label_every = int(round(len(labels)/10))

    throttle_line_chart = pygal.Line(width=500,height=300,show_legend=True,style=CleanStyle,x_label_rotation=20,label_font_size=12,x_labels_major_every=label_every,show_only_major_dots=True,show_minor_x_labels=False)
    throttle_line_chart.title = "Population"
    throttle_line_chart.x_labels = labels

    for data_set in data_lists:
        throttle_line_chart.add(str(data_set[0]), data_set[1:])

    raw_graph = throttle_line_chart.render()            
    return raw_graph


def getPopulationList(query=None, handler=None):
    # Get collection list from current DB
    collection_list = _mongo_db.collection_names(include_system_collections=False)

    # HTML Header
    html_header = "<html>\n\
    <head>\n\
        <meta http-equiv=\"refresh\" content=\"20\">\n\
        <meta http-equiv=\"X-UA-Compatible\" content=\"chrome=1\">\n\
    </head>\n\
    <body>\n"

    # HTML Footer
    html_footer = "</body>\n</html>"

    # Add to each returned collection
    link_prefix =  "http://" + str(handler.headers['Host']) + "/action/getpop?population_id="
 
    html_body = "Display all recorded population census data:<br>\n<br>\n"    
    for collection in collection_list:
        if "census" in collection:
             html_body = html_body + "<a href=" + link_prefix + str(collection) + ">" + str(collection) + "</a><br>\n"

    response = html_header + html_body + html_footer

    return(200, response)



def _mongoConnect():
    try:
        mongo_client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        mongo_db = mongo_client[MONGO_DB]
        return(mongo_client, mongo_db)

    except:
        assert False, "Error: Unknown error occurred while connecting to MongoDB"

_mongo_client, _mongo_db = _mongoConnect()
