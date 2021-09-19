import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBIMufMrfewD-4T9otfhBPWUp9xPqH-RKw')

from datetime import datetime, timedelta

def route():
    # locations = ["Fort Canning Park, Singapore",
    #       "Chinatown Buddha Tooth Relic Temple", 
    #       "Sentosa Island, Singapore", 
    #       "National Gallery Singapore", 
    #       "Boat Quay @ Bonham Street, Singapore 049782",
    #       "Botanic Garden, Singapore",
    #       "Raffles Hotel, Singapore"]
    
    locations = ['1.339398, 103.970784','1.339966, 103.972114','1.341028, 103.968166' ]

    waypoints = locations[1:-1]

    results = gmaps.directions(origin = locations[0],
                                            destination = locations[-1],                                     
                                            waypoints = waypoints,
                                            optimize_waypoints = True,
                                            departure_time=datetime.now() + timedelta(hours=1))


    marker_points = []
    waypoints = []

    #extract the location points from the previous directions function

    for leg in results[0]["legs"]:
        leg_start_loc = leg["start_location"]
        marker_points.append(f'{leg_start_loc["lat"]},{leg_start_loc["lng"]}')
        for step in leg["steps"]:
            end_loc = step["end_location"]
            waypoints.append(f'{end_loc["lat"]},{end_loc["lng"]}')
    last_stop = results[0]["legs"][-1]["end_location"]
    marker_points.append(f'{last_stop["lat"]},{last_stop["lng"]}')
            
    markers = [ "color:blue|size:mid|label:" + chr(65+i) + "|" 
            + r for i, r in enumerate(marker_points)]
    result_map = gmaps.static_map(
                    center = waypoints[0],
                    scale=2, 
                    zoom=13,
                    size=[640, 640], 
                    format="jpg", 
                    maptype="roadmap",
                    markers=markers,
                    path="color:0x0000ff|weight:2|" + "|".join(waypoints))

    with open("driving_route_map.jpg", "wb") as img:
        for chunk in result_map:
            img.write(chunk)
            
