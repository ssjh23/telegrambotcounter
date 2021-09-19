"""Capacited Vehicles Routing Problem (CVRP)."""

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import re
import pyrebase
import fbaseConfig

def coord_convert ():
	ls_new = []
	ls = [
			['''1°27'00.1"N''', '''103°48'10.1"E'''],
			['''1°26'52.8"N''', '''103°48'04.3"E'''],
			['''1°26'53.0"N''', '''103°48'08.5"E'''],
			['''1°26'49.0"N''', '''103°48'17.2"E'''],
			['''1°26'48.9"N''', '''103°48'02.1"E'''],
			['''1°26'39.7"N''', '''103°48'04.7"E'''],
			['''1°26'35.2"N''', '''103°48'09.6"E'''],
			['''1°26'52.7"N''', '''103°47'55.8"E'''],
			['''1°26'42.4"N''', '''103°47'56.6"E'''],
			['''1°26'30.1"N''', '''103°47'59.3"E'''],
			['''1°26'45.1"N''', '''103°47'48.3"E'''],
			['''1°26'39.9"N''', '''103°47'46.1"E'''],
			['''1°26'36.0"N''', '''103°47'55.0"E'''],
			['''1°26'44.2"N''', '''103°47'39.6"E'''],
			['''1°26'36.2"N''', '''103°47'43.0"E'''],
			['''1°26'28.8"N''', '''103°47'46.3"E''']
		]
	for i in ls:
		temp = ''
		for j in i:
			deg, minutes, seconds, direction =  re.split('[°\'"]', j)
			value = str((float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1))
			temp += str(value) + ', '
		temp = temp[:-2]
		ls_new.append(temp)
	
	return ls_new

def create_data_model():
    firebaseConfig = fbaseConfig.firebaseConfig
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    bin = db.child("Bin1").get()
    database_value = None
    for data in bin.each():
        if data.key() == 'distance':
            database_value = float(data.val())
    capacities = [0, 6, 10, 9, 5, 2, 6, 8, 2, 9, 3, 5, 8, 10, 2, database_value]
    demands_ls = [0,]
    unedited_matrix = [
            [
                0, 550, 1200, 1300, 850, 1100, 1400, 700, 1400, 1800, 1200, 1500, 1400, 1800,
                2200, 2200
            ],
            #1
            [
                550, 0, 1000, 1100, 700, 900, 1600, 550, 1400, 1800, 1000, 1100, 1000, 1700,
                1400, 2100
            ],
            #2
            [
                850, 1000, 0, 650, 1100, 1000, 1600, 1100, 1500, 1800, 1400, 1500, 1400,
                2600, 1800, 3000
            ],
            #3
            [
                700, 1200, 650, 0, 1300, 800, 1300, 1400, 2100, 1400, 1300, 2000, 1900, 2300,
                2700, 2700
            ],
            #4
            [
                1400, 700, 1100, 1200, 0, 1000, 1100, 500, 950, 1300, 900, 1000, 900, 1200,
                1300, 1700
            ],
            #5
            [
                1200, 850, 1000, 800, 950, 0, 1300, 900, 1300, 1400, 1200, 1400, 1300, 1600,
                1700, 2000
            ],
            #6
            [
                1700, 1400, 1700, 1900, 1200, 1300, 0, 1100, 900, 550, 1200, 1300, 1200, 1500,
                1600, 1700
            ],
            #7
            [
                1400, 550, 1000, 1100, 500, 900, 900, 0, 750, 1100, 700, 800, 700, 1000,
                1100, 1500
            ],
            #8
            [
                1800, 1100, 1500, 1500, 900, 1300, 750, 750, 0, 1000, 2000, 850, 450, 1100,
                1000, 1100
            ],
            #9
            [
                2100, 1400, 1800, 1900, 1300, 1500, 550, 1100, 950, 0, 1200, 1400, 1300, 1600,
                1700, 2000
            ],
            #10
            [
                2000, 1200, 1600, 1700, 1100, 1500, 1300, 900, 2000, 1500, 0, 1600, 1800,
                1100, 1500, 1900
            ],
            #11
            [
                2400, 1100, 1500, 1500, 1000, 1400, 1200, 800, 850, 1400, 1000, 0, 600,
                650, 350, 700
            ],
            #12
            [
                1800, 1000, 1400, 1500, 900, 1300, 1100, 700, 450, 1400, 1800, 600, 0, 800,
                750, 900
            ],
            #13
            [
                2100, 1400, 1800, 1800, 1200, 1600, 1400, 1000, 1100, 1600, 1100, 650, 800, 0,
                550, 900
            ],
            #14
            [
                2200, 1400, 1800, 1900, 1300, 1700, 1400, 1100, 1000, 1400, 1500, 350, 750, 550,
                0, 600
            ],
            #15
            [
                2500, 1800, 2200, 2200, 1600, 2100, 1500, 1500, 1100, 1700, 1900, 700, 900,
                900, 600, 0
            ]
        ]
    distance_matrix_ls = [
            [
                0, 550, 1200, 1300, 850, 1100, 1400, 700, 1400, 1800, 1200, 1500, 1400, 1800,
                2200, 2200
            ]
        ]

    unedited_coordinates = coord_convert()
    coordinates = [unedited_coordinates[0]]

    for i in range(len(capacities)):
        if capacities[i] < 8:
            pass
        else:
            demands_ls.append(capacities[i])
            distance_matrix_ls.append(unedited_matrix[i])
            coordinates.append(unedited_coordinates[i])

    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_matrix_ls
    data['demands'] = demands_ls
    data['vehicle_capacities'] = [40, 40, 40, 40]
    data['num_vehicles'] = 4
    data['depot'] = 0
    data['coordinates'] = coordinates
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f'Objective: {solution.ObjectiveValue()}')
    total_distance = 0
    total_load = 0
    coord_output = []
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load = 0
        #coord_output = []
        plan_output= []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            print(data['coordinates'][node_index])
            plan_output.append(data['coordinates'][node_index])
            print(plan_output)
            print('---')
            #plan_output += ' {0} Load({1}) -> '.format(node_index, route_load)
            #coord_output.append(data['coordinates'][node_index])
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output.append(data['coordinates'][manager.IndexToNode(index)])
        #plan_output += ' {0} Load({1})\n'.format(manager.IndexToNode(index),
        #                                          route_load)
        # plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        # plan_output += 'Load of the route: {}\n'.format(route_load)
        if len(plan_output) == 2:
            pass
        else:
            coord_output.append(plan_output)
        total_distance += route_distance
        total_load += route_load
    print(coord_output)
    print('length:' + str(len(coord_output)))
    print('Total distance of all routes: {}m'.format(total_distance))
    print('Total load of all routes: {}'.format(total_load))
    firebaseConfig = fbaseConfig.firebaseConfig
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    data = {'Route_List' : coord_output, "Total_Avail_Routes": len(coord_output)}
    db.child('Route_Data').set(data)
    return coord_output

def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.FromSeconds(1)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)


if __name__ == '__main__':
    main()