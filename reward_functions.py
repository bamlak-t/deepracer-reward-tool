'''
    Contains multiple reward functions to be checked
'''

import numpy as np
import useful_functions as uf

def default(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    return float(reward)


def stepsTest(params):
    '''
    Test params
    '''

    # Read input parameters
    steps = params['steps']
    if steps > 80:
        reward = 1.0
    elif steps > 40 and steps <= 80:
        reward = 0.5
    else:
        reward = 1e-3  

    return float(reward)

def progressTest(params):
    '''
    Test params
    '''

    # Read input parameters
    progress = params['progress']

    return 1*float(progress)

def leftOfCenterTest(params):
    '''
    Test params
    '''
    
    # Read input parameters
    leftOfCenter = params['is_left_of_center']

    if leftOfCenter:
        reward = 1.0
    else:
        reward = 1e-3  

    return float(reward)

def offTrackTest(params):
    '''
    Test params
    '''
    
    # Read input parameters
    offTrack = params['is_offtrack']
    
    if offTrack:
        reward = 1.0
    else:
        reward = 1e-3  

    return float(reward)

import math

def eg1(params):
    ###############################################################################
    '''
    Example of using waypoints and heading to make the car point in the right direction
    '''

    # Read input variables
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Initialize the reward with typical value
    reward = 1.0

    # Calculate the direction of the center line based on the closest waypoints
    next_point = closest_waypoints[1]
    prev_point = closest_waypoints[0]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    return float(reward)

def racingLine(params):
    '''
    Test params
    ''',
    offset = np.array([( 0.,-0.1  ),
        ( 0.,-0.125),
        ( 0.,-0.15 ),
        ( 0.,-0.175),
        ( 0.,-0.2  ),
        ( 0.,-0.225),
        ( 0.,-0.25 ),
        ( 0.,-0.275),
        ( 0.,-0.3  ),
        ( 0.,-0.325),
        ( 0.,-0.35 ),
        ( 0.,-0.375),
        ( 0.,-0.35 ),
        ( 0.,-0.325),
        ( 0.,-0.3  ),
        ( 0.,-0.275),
        ( 0.,-0.25 ),
        ( 0.,-0.2  ),
        ( 0.,-0.15 ),
        ( 0.,-0.1  ),
        ( 0.,-0.05 ),
        ( 0., 0.   ),
        ( 0., 0.1  ),
        ( 0., 0.2  ),
        ( 0., 0.3  ),
        ( 0., 0.4  ),
        (-0.15, 0.3  ),
        (-0.2,0.2  ),
        (-0.25, 0.1  ),
        (-0.3,0.   ),
        (-0.25,0.   ),
        (-0.2,0.   ),
        (-0.15,0.   ),
        (-0.1,0.   ),
        (-0.05,0.   ),
        ( 0., 0.   ),
        ( 0.05,0.   ),
        ( 0.1,0.   ),
        ( 0.15,0.   ),
        ( 0.2,0.   ),
        ( 0.25,0.   ),
        ( 0.275,0.   ),
        ( 0.3,0.   ),
        ( 0.25,0.   ),
        ( 0.2,0.   ),
        ( 0.2,0.   ),
        ( 0.1,0.   ),
        ( 0., 0.   ),
        ( 0.,-0.1  ),
        ( 0.,-0.2  ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.2  ),
        ( 0.,-0.15 ),
        ( 0.,-0.1  ),
        ( 0., 0.   ),
        ( 0., 0.15 ),
        ( 0., 0.2  ),
        ( 0., 0.25 ),
        ( 0., 0.225),
        ( 0., 0.2  ),
        ( 0., 0.1  ),
        ( 0.1,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0., 0.1  ),
        ( 0., 0.15 ),
        ( 0., 0.2  ),
        ( 0., 0.25 ),
        ( 0., 0.3  ),
        ( 0., 0.25 ),
        ( 0., 0.2  ),
        (-0.1,0.   ),
        (-0.15,0.   ),
        (-0.2,0.   ),
        (-0.25,0.   ),
        (-0.25,0.   ),
        (-0.25,0.   ),
        ( 0., 0.1  ),
        ( 0., 0.   ),
        ( 0.,-0.1  ),
        ( 0.,-0.2  ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.2  ),
        ( 0.,-0.1  ),
        ( 0., 0.   ),
        ( 0., 0.1  ),
        ( 0.1,0.   ),
        ( 0.2,0.   ),
        ( 0.25,0.   ),
        ( 0.25,0.   ),
        ( 0.25,0.   ),
        ( 0.25,0.   ),
        ( 0.2,0.   ),
        ( 0.15,0.   ),
        ( 0.1,0.   ),
        ( 0., 0.   ),
        ( 0.,-0.1  ),
        ( 0.,-0.2  ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.2  ),
        ( 0.,-0.15 ),
        ( 0.,-0.1  ),
        ( 0., 0.   ),
        (-0.1,0.   ),
        (-0.125,0.  ),
        (-0.15,0.   ),
        (-0.175,0.   ),
        (-0.2,0.   ),
        (-0.225,0.   ),
        (-0.25,0.   ),
        (-0.275,0.   ),
        (-0.25,0.   ),
        (-0.225,0.   ),
        (-0.2,0.   ),
        (-0.15,0.   ),
        (-0.1,0.   ),
        (-0.05,0.   ),
        ( 0., 0.   ),
        ( 0., 0.   ),
        ( 0.,-0.05 ),
        ( 0.,-0.1  )])

    # print(racingLineCoords)

    # Read input parameters
    track_width = params['track_width']
    center = params['waypoints']
    steps = params['steps']
    x = params['x']
    y = params['y']

    final = center + offset

    # print(offset)
    

    distance_from_racing_line = uf.getTwoPointDistance(final[steps-1][0], x, final[steps-1][1], y)
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_racing_line <= marker_1:
        reward = 1.0
    elif distance_from_racing_line <= marker_2:
        reward = 0.5
    elif distance_from_racing_line <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    return float(reward)


def racingLine2(params):
    '''
    Test params
    ''',
    offset = np.array([( 0.,-0.1  ),
        ( 0.,-0.125),
        ( 0.,-0.15 ),
        ( 0.,-0.175),
        ( 0.,-0.2  ),
        ( 0.,-0.225),
        ( 0.,-0.25 ),
        ( 0.,-0.275),
        ( 0.,-0.3  ),
        ( 0.,-0.325),
        ( 0.,-0.35 ),
        ( 0.,-0.375),
        ( 0.,-0.35 ),
        ( 0.,-0.325),
        ( 0.,-0.3  ),
        ( 0.,-0.275),
        ( 0.,-0.25 ),
        ( 0.,-0.2  ),
        ( 0.,-0.15 ),
        ( 0.,-0.1  ),
        ( 0.,-0.05 ),
        ( 0., 0.   ),
        ( 0., 0.1  ),
        ( 0., 0.2  ),
        ( 0., 0.3  ),
        ( 0., 0.4  ),
        (-0.15, 0.3  ),
        (-0.2,0.2  ),
        (-0.25, 0.1  ),
        (-0.3,0.   ),
        (-0.25,0.   ),
        (-0.2,0.   ),
        (-0.15,0.   ),
        (-0.1,0.   ),
        (-0.05,0.   ),
        ( 0., 0.   ),
        ( 0.05,0.   ),
        ( 0.1,0.   ),
        ( 0.15,0.   ),
        ( 0.2,0.   ),
        ( 0.25,0.   ),
        ( 0.275,0.   ),
        ( 0.3,0.   ),
        ( 0.25,0.   ),
        ( 0.2,0.   ),
        ( 0.2,0.   ),
        ( 0.1,0.   ),
        ( 0., 0.   ),
        ( 0.,-0.1  ),
        ( 0.,-0.2  ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.2  ),
        ( 0.,-0.15 ),
        ( 0.,-0.1  ),
        ( 0., 0.   ),
        ( 0., 0.15 ),
        ( 0., 0.2  ),
        ( 0., 0.25 ),
        ( 0., 0.225),
        ( 0., 0.2  ),
        ( 0., 0.1  ),
        ( 0.1,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0.15,0.   ),
        ( 0., 0.1  ),
        ( 0., 0.15 ),
        ( 0., 0.2  ),
        ( 0., 0.25 ),
        ( 0., 0.3  ),
        ( 0., 0.25 ),
        ( 0., 0.2  ),
        (-0.1,0.   ),
        (-0.15,0.   ),
        (-0.2,0.   ),
        (-0.25,0.   ),
        (-0.25,0.   ),
        (-0.25,0.   ),
        ( 0., 0.1  ),
        ( 0., 0.   ),
        ( 0.,-0.1  ),
        ( 0.,-0.2  ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.2  ),
        ( 0.,-0.1  ),
        ( 0., 0.   ),
        ( 0., 0.1  ),
        ( 0.1,0.   ),
        ( 0.2,0.   ),
        ( 0.25,0.   ),
        ( 0.25,0.   ),
        ( 0.25,0.   ),
        ( 0.25,0.   ),
        ( 0.2,0.   ),
        ( 0.15,0.   ),
        ( 0.1,0.   ),
        ( 0., 0.   ),
        ( 0.,-0.1  ),
        ( 0.,-0.2  ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.25 ),
        ( 0.,-0.2  ),
        ( 0.,-0.15 ),
        ( 0.,-0.1  ),
        ( 0., 0.   ),
        (-0.1,0.   ),
        (-0.125,0.   ),
        (-0.15,0.   ),
        (-0.175,0.   ),
        (-0.2,0.   ),
        (-0.225,0.   ),
        (-0.25,0.   ),
        (-0.275,0.   ),
        (-0.25,0.   ),
        (-0.225,0.   ),
        (-0.2,0.   ),
        (-0.15,0.   ),
        (-0.1,0.   ),
        (-0.05,0.   ),
        ( 0., 0.   ),
        ( 0., 0.   ),
        ( 0.,-0.05 ),
        ( 0.,-0.1  )])

    # Read input parameters
    track_width = params['track_width']
    center = params['waypoints']
    progress = params['progress']
    x = params['x']
    y = params['y']

    final = center
    if len(center) == len(offset):
        final = center + offset
    
    traveled = int((len(center)*progress)//100)

    distance_from_racing_line = ((final[traveled-1][0]-x)**2 + (final[traveled-1][1]-y)**2)**0.5

    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_racing_line <= marker_1:
        reward = 1.0
    elif distance_from_racing_line <= marker_2:
        reward = 0.5
    elif distance_from_racing_line <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    return float(reward)

def racingLine3(params):
    '''
    Test params
    ''',
    final = np.array([[-4.23422983, -1.97569107],
       [-4.00403894, -2.1101672 ],
       [-3.75792399, -2.23127571],
       [-3.49841778, -2.34049645],
       [-3.22823755, -2.43972365],
       [-2.94990001, -2.53094507],
       [-2.66556755, -2.61605529],
       [-2.3767669 , -2.69635387],
       [-2.08522388, -2.77176159],
       [-1.79306548, -2.84210459],
       [-1.50095216, -2.90728042],
       [-1.20917298, -2.96721989],
       [-0.91790165, -3.02180079],
       [-0.62727416, -3.07085551],
       [-0.33744276, -3.11398917],
       [-0.04856419, -3.15080972],
       [ 0.23919538, -3.1809266 ],
       [ 0.52563487, -3.20382579],
       [ 0.81041492, -3.21843649],
       [ 1.09313456, -3.22367016],
       [ 1.37324675, -3.21810188],
       [ 1.65000797, -3.19992455],
       [ 1.92219272, -3.16622047],
       [ 2.18815501, -3.11367214],
       [ 2.44546382, -3.03798069],
       [ 2.69055724, -2.93379282],
       [ 2.91774703, -2.79400185],
       [ 3.13192127, -2.63130587],
       [ 3.33447978, -2.44951262],
       [ 3.5264185 , -2.25153197],
       [ 3.70802159, -2.03989531],
       [ 3.87906604, -1.81767844],
       [ 4.0392887 , -1.58810701],
       [ 4.18826198, -1.35361416],
       [ 4.32593548, -1.11601485],
       [ 4.45250935, -0.87649938],
       [ 4.56793673, -0.63577564],
       [ 4.67226587, -0.39429417],
       [ 4.76554604, -0.15231786],
       [ 4.8477954 ,  0.09001045],
       [ 4.91876786,  0.33261771],
       [ 4.97792922,  0.57545232],
       [ 5.02374878,  0.81843785],
       [ 5.05448683,  1.06136688],
       [ 5.06754094,  1.3037448 ],
       [ 5.05913784,  1.54444284],
       [ 5.02390732,  1.78092354],
       [ 4.95576818,  2.00833294],
       [ 4.84849507,  2.21908359],
       [ 4.69477824,  2.40149012],
       [ 4.51456284,  2.56366467],
       [ 4.31132686,  2.70615958],
       [ 4.08778828,  2.82931657],
       [ 3.84595495,  2.93282717],
       [ 3.58809992,  3.01627617],
       [ 3.31680756,  3.07848798],
       [ 3.03604616,  3.11768079],
       [ 2.75202407,  3.13213931],
       [ 2.47206899,  3.12173417],
       [ 2.20302863,  3.08617606],
       [ 1.94996878,  3.02664376],
       [ 1.71699289,  2.94389781],
       [ 1.50756998,  2.83883866],
       [ 1.32446882,  2.71282403],
       [ 1.17342985,  2.56558298],
       [ 1.05961967,  2.39863534],
       [ 0.9905943 ,  2.21397723],
       [ 0.97857261,  2.01580077],
       [ 1.01202563,  1.81380341],
       [ 1.08315912,  1.61286801],
       [ 1.18394428,  1.41531277],
       [ 1.30610361,  1.2215021 ],
       [ 1.43980752,  1.03014356],
       [ 1.57154221,  0.84305822],
       [ 1.68350947,  0.65034231],
       [ 1.75742031,  0.44837214],
       [ 1.76890383,  0.24111879],
       [ 1.73191761,  0.03960609],
       [ 1.65442255, -0.15084839],
       [ 1.541982  , -0.32665779],
       [ 1.39897478, -0.4849981 ],
       [ 1.2294892 , -0.62367845],
       [ 1.03697306, -0.74043873],
       [ 0.82515242, -0.83330843],
       [ 0.59820564, -0.90087749],
       [ 0.36066863, -0.94267126],
       [ 0.11684933, -0.95832282],
       [-0.12908098, -0.94811868],
       [-0.37336901, -0.91315535],
       [-0.61277665, -0.8545391 ],
       [-0.84439334, -0.77307136],
       [-1.06455629, -0.6677498 ],
       [-1.26916352, -0.5378391 ],
       [-1.45273223, -0.38172649],
       [-1.6078238 , -0.19718615],
       [-1.72205691,  0.01958492],
       [-1.80638776,  0.25584981],
       [-1.86760745,  0.50565732],
       [-1.91320796,  0.76405276],
       [-1.9506677 ,  1.02678721],
       [-1.9891084 ,  1.29170579],
       [-2.03372888,  1.5529323 ],
       [-2.08963949,  1.80700082],
       [-2.16106291,  2.05026832],
       [-2.25184913,  2.27824211],
       [-2.36442395,  2.4861791 ],
       [-2.50020156,  2.66866828],
       [-2.65946644,  2.81924903],
       [-2.84123993,  2.92878287],
       [-3.0410043 ,  2.98339742],
       [-3.24701507,  2.98920615],
       [-3.45259763,  2.95486795],
       [-3.65407743,  2.88521894],
       [-3.8487455 ,  2.78307508],
       [-4.03434506,  2.65061037],
       [-4.20895255,  2.48983955],
       [-4.37113515,  2.30323148],
       [-4.51975047,  2.09333969],
       [-4.65437467,  1.86348964],
       [-4.7748846 ,  1.6169849 ],
       [-4.8811759 ,  1.35697136],
       [-4.97250573,  1.08631645],
       [-5.04812648,  0.80851393],
       [-5.10704702,  0.52734878],
       [-5.14814935,  0.24656236],
       [-5.17028775, -0.03056411],
       [-5.17287916, -0.30166095],
       [-5.15389081, -0.56446373],
       [-5.11097123, -0.81675144],
       [-5.0412801 , -1.05604883],
       [-4.94121419, -1.27918669],
       [-4.80351525, -1.4800066 ],
       [-4.63709856, -1.66200158],
       [-4.44621415, -1.82675882],
       [-4.23422983, -1.97569107]])

    # Read input parameters
    track_width = params['track_width']
    # center = params['waypoints']
    progress = params['progress']
    x = params['x']
    y = params['y']
    isOffTrack = params["is_offtrack"]
    speed = params["speed"]
    allWheelsOnTrack = params["all_wheels_on_track"]
    traveled = int((len(final)*progress)//100)

    distance_from_racing_line = ((final[traveled-1][0]-x)**2 + (final[traveled-1][1]-y)**2)**0.5
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width/1.5
    marker_2 = 0.25 * track_width/1.5
    marker_3 = 0.5 * track_width/1.5
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_racing_line <= marker_1:
        reward = 1.0
    elif distance_from_racing_line <= marker_2:
        reward = 0.5
    elif distance_from_racing_line <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    if isOffTrack:
        reward *= 0.3
    
    if allWheelsOnTrack:
        reward *= 0.9

    if speed<=1:
        reward *= 0.3
    elif speed<2:
        reward *= 0.5
    elif speed<3:
        reward *= 0.7

    reward *= (0.7 + (progress * 0.003))

    return float(reward)

class Reward:
    def __init__(self, verbose=False):
        self.first_racingpoint_index = 0
        self.verbose = verbose

    def reward_function(self, params):

        # Import package (needed for heading)
        import math

        ################## HELPER FUNCTIONS ###################

        def dist_2_points(x1, x2, y1, y2):
            return abs(abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

        def closest_2_racing_points_index(racing_coords, car_coords):

            # Calculate all distances to racing points
            distances = []
            for i in range(len(racing_coords)):
                distance = dist_2_points(x1=racing_coords[i][0], x2=car_coords[0],
                                         y1=racing_coords[i][1], y2=car_coords[1])
                distances.append(distance)

            # Get index of the closest racing point
            closest_index = distances.index(min(distances))

            # Get index of the second closest racing point
            distances_no_closest = distances.copy()
            distances_no_closest[closest_index] = 999
            second_closest_index = distances_no_closest.index(
                min(distances_no_closest))

            return [closest_index, second_closest_index]

        def dist_to_racing_line(closest_coords, second_closest_coords, car_coords):
            
            # Calculate the distances between 2 closest racing points
            a = abs(dist_2_points(x1=closest_coords[0],
                                  x2=second_closest_coords[0],
                                  y1=closest_coords[1],
                                  y2=second_closest_coords[1]))

            # Distances between car and closest and second closest racing point
            b = abs(dist_2_points(x1=car_coords[0],
                                  x2=closest_coords[0],
                                  y1=car_coords[1],
                                  y2=closest_coords[1]))
            c = abs(dist_2_points(x1=car_coords[0],
                                  x2=second_closest_coords[0],
                                  y1=car_coords[1],
                                  y2=second_closest_coords[1]))

            # Calculate distance between car and racing line (goes through 2 closest racing points)
            # try-except in case a=0 (rare bug in DeepRacer)
            try:
                distance = abs(-(a**4) + 2*(a**2)*(b**2) + 2*(a**2)*(c**2) -
                               (b**4) + 2*(b**2)*(c**2) - (c**4))**0.5 / (2*a)
            except:
                distance = b

            return distance

        # Calculate which one of the closest racing points is the next one and which one the previous one
        def next_prev_racing_point(closest_coords, second_closest_coords, car_coords, heading):

            # Virtually set the car more into the heading direction
            heading_vector = [math.cos(math.radians(
                heading)), math.sin(math.radians(heading))]
            new_car_coords = [car_coords[0]+heading_vector[0],
                              car_coords[1]+heading_vector[1]]

            # Calculate distance from new car coords to 2 closest racing points
            distance_closest_coords_new = dist_2_points(x1=new_car_coords[0],
                                                        x2=closest_coords[0],
                                                        y1=new_car_coords[1],
                                                        y2=closest_coords[1])
            distance_second_closest_coords_new = dist_2_points(x1=new_car_coords[0],
                                                               x2=second_closest_coords[0],
                                                               y1=new_car_coords[1],
                                                               y2=second_closest_coords[1])

            if distance_closest_coords_new <= distance_second_closest_coords_new:
                next_point_coords = closest_coords
                prev_point_coords = second_closest_coords
            else:
                next_point_coords = second_closest_coords
                prev_point_coords = closest_coords

            return [next_point_coords, prev_point_coords]

        def racing_direction_diff(closest_coords, second_closest_coords, car_coords, heading):

            # Calculate the direction of the center line based on the closest waypoints
            next_point, prev_point = next_prev_racing_point(closest_coords,
                                                            second_closest_coords,
                                                            car_coords,
                                                            heading)

            # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
            track_direction = math.atan2(
                next_point[1] - prev_point[1], next_point[0] - prev_point[0])

            # Convert to degree
            track_direction = math.degrees(track_direction)

            # Calculate the difference between the track direction and the heading direction of the car
            direction_diff = abs(track_direction - heading)
            if direction_diff > 180:
                direction_diff = 360 - direction_diff

            return direction_diff

        # Gives back indexes that lie between start and end index of a cyclical list 
        # (start index is included, end index is not)
        def indexes_cyclical(start, end, array_len):

            if end < start:
                end += array_len

            return [index % array_len for index in range(start, end)]

        # Calculate how long car would take for entire lap, if it continued like it did until now
        def projected_time(first_index, closest_index, step_count, times_list):

            # Calculate how much time has passed since start
            current_actual_time = (step_count-1) / 15

            # Calculate which indexes were already passed
            indexes_traveled = indexes_cyclical(first_index, closest_index, len(times_list))

            # Calculate how much time should have passed if car would have followed optimals
            current_expected_time = sum([times_list[i] for i in indexes_traveled])

            # Calculate how long one entire lap takes if car follows optimals
            total_expected_time = sum(times_list)

            # Calculate how long car would take for entire lap, if it continued like it did until now
            try:
                projected_time = (current_actual_time/current_expected_time) * total_expected_time
            except:
                projected_time = 9999

            return projected_time

        #################### RACING LINE ######################

        # Optimal racing line for the Spain track
        # Each row: [x,y,speed,timeFromPreviousPoint]
        racing_track = [[-4.23423, -1.97569, 2.81794, 0.09194],
                        [-4.00404, -2.11017, 3.09476, 0.08614],
                        [-3.75792, -2.23128, 3.45412, 0.07941],
                        [-3.49842, -2.3405, 3.93901, 0.07148],
                        [-3.22824, -2.43972, 4.0, 0.07196],
                        [-2.9499, -2.53095, 4.0, 0.07323],
                        [-2.66557, -2.61606, 4.0, 0.0742],
                        [-2.37677, -2.69635, 4.0, 0.07494],
                        [-2.08522, -2.77176, 4.0, 0.07528],
                        [-1.79307, -2.8421, 4.0, 0.07513],
                        [-1.50095, -2.90728, 4.0, 0.07482],
                        [-1.20917, -2.96722, 4.0, 0.07447],
                        [-0.9179, -3.0218, 4.0, 0.07409],
                        [-0.62727, -3.07086, 4.0, 0.07368],
                        [-0.33744, -3.11399, 4.0, 0.07326],
                        [-0.04856, -3.15081, 3.92736, 0.07415],
                        [0.2392, -3.18093, 3.47957, 0.08315],
                        [0.52563, -3.20383, 3.09799, 0.09275],
                        [0.81041, -3.21844, 2.73748, 0.10417],
                        [1.09313, -3.22367, 2.416, 0.11704],
                        [1.37325, -3.2181, 2.12329, 0.13195],
                        [1.65001, -3.19992, 2.12329, 0.13063],
                        [1.92219, -3.16622, 2.12329, 0.12917],
                        [2.18816, -3.11367, 2.12329, 0.12768],
                        [2.44546, -3.03798, 2.12329, 0.12632],
                        [2.69056, -2.93379, 2.12329, 0.12543],
                        [2.91775, -2.794, 2.62896, 0.10147],
                        [3.13192, -2.63131, 2.89293, 0.09297],
                        [3.33448, -2.44951, 3.15833, 0.08618],
                        [3.52642, -2.25153, 3.39834, 0.08114],
                        [3.70802, -2.0399, 3.64722, 0.07646],
                        [3.87907, -1.81768, 3.8965, 0.07197],
                        [4.03929, -1.58811, 4.0, 0.06999],
                        [4.18826, -1.35361, 3.99974, 0.06946],
                        [4.32594, -1.11601, 3.88523, 0.07068],
                        [4.45251, -0.8765, 3.73265, 0.07258],
                        [4.56794, -0.63578, 3.45764, 0.07721],
                        [4.67227, -0.39429, 3.20685, 0.08203],
                        [4.76555, -0.15232, 2.92543, 0.08865],
                        [4.8478, 0.09001, 2.62591, 0.09745],
                        [4.91877, 0.33262, 2.31808, 0.10905],
                        [4.97793, 0.57545, 2.05185, 0.12181],
                        [5.02375, 0.81844, 1.82722, 0.13532],
                        [5.05449, 1.06137, 1.6198, 0.15117],
                        [5.06754, 1.30374, 1.6198, 0.14985],
                        [5.05914, 1.54444, 1.6198, 0.14869],
                        [5.02391, 1.78092, 1.6198, 0.14761],
                        [4.95577, 2.00833, 1.6198, 0.14656],
                        [4.8485, 2.21908, 1.6198, 0.14599],
                        [4.69478, 2.40149, 2.10171, 0.1135],
                        [4.51456, 2.56366, 2.2625, 0.10716],
                        [4.31133, 2.70616, 2.42928, 0.10218],
                        [4.08779, 2.82932, 2.57157, 0.09925],
                        [3.84595, 2.93283, 2.71805, 0.09678],
                        [3.5881, 3.01628, 2.59718, 0.10435],
                        [3.31681, 3.07849, 2.41274, 0.11536],
                        [3.03605, 3.11768, 2.21927, 0.12774],
                        [2.75202, 3.13214, 2.04759, 0.13889],
                        [2.47207, 3.12173, 1.7967, 0.15592],
                        [2.20303, 3.08618, 1.61806, 0.16772],
                        [1.94997, 3.02664, 1.45007, 0.17928],
                        [1.71699, 2.9439, 1.3, 0.19018],
                        [1.50757, 2.83884, 1.3, 0.18023],
                        [1.32447, 2.71282, 1.3, 0.17098],
                        [1.17343, 2.56558, 1.3, 0.16226],
                        [1.05962, 2.39864, 1.3, 0.15542],
                        [0.99059, 2.21398, 1.3, 0.15164],
                        [0.97857, 2.0158, 1.50801, 0.13166],
                        [1.01203, 1.8138, 1.73324, 0.11813],
                        [1.08316, 1.61287, 1.77738, 0.11993],
                        [1.18394, 1.41531, 1.34733, 0.16461],
                        [1.3061, 1.2215, 1.34733, 0.17004],
                        [1.43981, 1.03014, 1.34733, 0.17326],
                        [1.57154, 0.84306, 1.34733, 0.16983],
                        [1.68351, 0.65034, 1.34733, 0.16542],
                        [1.75742, 0.44837, 1.34733, 0.15963],
                        [1.7689, 0.24112, 1.48553, 0.13973],
                        [1.73192, 0.03961, 1.59293, 0.12862],
                        [1.65442, -0.15085, 1.69513, 0.1213],
                        [1.54198, -0.32666, 1.79639, 0.11617],
                        [1.39897, -0.485, 1.90698, 0.11188],
                        [1.22949, -0.62368, 1.99951, 0.10952],
                        [1.03697, -0.74044, 2.09186, 0.10763],
                        [0.82515, -0.83331, 2.18699, 0.10576],
                        [0.59821, -0.90088, 2.29101, 0.10336],
                        [0.36067, -0.94267, 2.36234, 0.1021],
                        [0.11685, -0.95832, 2.26931, 0.10766],
                        [-0.12908, -0.94812, 2.0974, 0.11736],
                        [-0.37337, -0.91316, 1.91069, 0.12916],
                        [-0.61278, -0.85454, 1.69668, 0.14527],
                        [-0.84439, -0.77307, 1.69668, 0.14471],
                        [-1.06456, -0.66775, 1.69668, 0.14384],
                        [-1.26916, -0.53784, 1.69668, 0.14285],
                        [-1.45273, -0.38173, 1.69668, 0.14203],
                        [-1.60782, -0.19719, 1.69668, 0.14208],
                        [-1.72206, 0.01958, 2.10107, 0.11662],
                        [-1.80639, 0.25585, 2.50394, 0.10019],
                        [-1.86761, 0.50566, 3.06915, 0.0838],
                        [-1.91321, 0.76405, 2.5993, 0.10095],
                        [-1.95067, 1.02679, 2.28039, 0.11638],
                        [-1.98911, 1.29171, 2.02295, 0.13233],
                        [-2.03373, 1.55293, 1.80401, 0.1469],
                        [-2.08964, 1.807, 1.59415, 0.16319],
                        [-2.16106, 2.05027, 1.3896, 0.18245],
                        [-2.25185, 2.27824, 1.3896, 0.17659],
                        [-2.36442, 2.48618, 1.3896, 0.17016],
                        [-2.5002, 2.66867, 1.3896, 0.16369],
                        [-2.65947, 2.81925, 1.3896, 0.15773],
                        [-2.84124, 2.92878, 1.3896, 0.15272],
                        [-3.041, 2.9834, 1.48124, 0.13981],
                        [-3.24702, 2.98921, 1.6463, 0.12519],
                        [-3.4526, 2.95487, 1.78597, 0.1167],
                        [-3.65408, 2.88522, 1.90895, 0.11167],
                        [-3.84875, 2.78308, 2.03648, 0.10795],
                        [-4.03435, 2.65061, 2.17651, 0.10476],
                        [-4.20895, 2.48984, 2.34851, 0.10106],
                        [-4.37114, 2.30323, 2.53398, 0.09757],
                        [-4.51975, 2.09334, 2.77053, 0.09283],
                        [-4.65437, 1.86349, 3.01705, 0.08829],
                        [-4.77488, 1.61698, 3.24608, 0.08453],
                        [-4.88118, 1.35697, 3.14621, 0.08928],
                        [-4.97251, 1.08632, 2.87704, 0.09929],
                        [-5.04813, 0.80851, 2.61089, 0.11027],
                        [-5.10705, 0.52735, 2.35855, 0.1218],
                        [-5.14815, 0.24656, 2.12659, 0.13344],
                        [-5.17029, -0.03056, 1.85544, 0.14983],
                        [-5.17288, -0.30166, 1.85544, 0.14612],
                        [-5.15389, -0.56446, 1.85544, 0.14201],
                        [-5.11097, -0.81675, 1.85544, 0.13793],
                        [-5.04128, -1.05605, 1.85544, 0.13433],
                        [-4.94121, -1.27919, 1.85544, 0.1318],
                        [-4.80352, -1.48001, 2.10731, 0.11555],
                        [-4.6371, -1.662, 2.31234, 0.10665],
                        [-4.44621, -1.82676, 2.54781, 0.09897]]

        ################## INPUT PARAMETERS ###################

        # Read all input parameters
        all_wheels_on_track = params['all_wheels_on_track']
        x = params['x']
        y = params['y']
        distance_from_center = params['distance_from_center']
        is_left_of_center = params['is_left_of_center']
        heading = params['heading']
        progress = params['progress']
        steps = params['steps']
        speed = params['speed']
        steering_angle = params['steering_angle']
        track_width = params['track_width']
        waypoints = params['waypoints']
        closest_waypoints = params['closest_waypoints']
        is_offtrack = params['is_offtrack']

        ############### OPTIMAL X,Y,SPEED,TIME ################

        # Get closest indexes for racing line (and distances to all points on racing line)
        closest_index, second_closest_index = closest_2_racing_points_index(
            racing_track, [x, y])

        # Get optimal [x, y, speed, time] for closest and second closest index
        optimals = racing_track[closest_index]
        optimals_second = racing_track[second_closest_index]

        # Save first racingpoint of episode for later
        if self.verbose == True:
            self.first_racingpoint_index = 0 # this is just for testing purposes
        if steps == 1:
            self.first_racingpoint_index = closest_index

        ################ REWARD AND PUNISHMENT ################

        ## Define the default reward ##
        reward = 1

        ## Reward if car goes close to optimal racing line ##
        DISTANCE_MULTIPLE = 1
        dist = dist_to_racing_line(optimals[0:2], optimals_second[0:2], [x, y])
        distance_reward = max(1e-3, 1 - (dist/(track_width*0.5)))
        reward += distance_reward * DISTANCE_MULTIPLE

        ## Reward if speed is close to optimal speed ##
        SPEED_DIFF_NO_REWARD = 1
        SPEED_MULTIPLE = 2
        speed_diff = abs(optimals[2]-speed)
        if speed_diff <= SPEED_DIFF_NO_REWARD:
            # we use quadratic punishment (not linear) bc we're not as confident with the optimal speed
            # so, we do not punish small deviations from optimal speed
            speed_reward = (1 - (speed_diff/(SPEED_DIFF_NO_REWARD))**2)**2
        else:
            speed_reward = 0
        reward += speed_reward * SPEED_MULTIPLE

        # Reward if less steps
        REWARD_PER_STEP_FOR_FASTEST_TIME = 1.5
        STANDARD_TIME = 55
        FASTEST_TIME = 52
        times_list = [row[3] for row in racing_track]
        projected_time = projected_time(self.first_racingpoint_index, closest_index, steps, times_list)
        try:
            steps_prediction = projected_time * 15 + 1
            reward_prediction = max(1e-3, (-REWARD_PER_STEP_FOR_FASTEST_TIME*(FASTEST_TIME) /
                                           (STANDARD_TIME-FASTEST_TIME))*(steps_prediction-(STANDARD_TIME*15+1)))
            steps_reward = min(REWARD_PER_STEP_FOR_FASTEST_TIME, reward_prediction / steps_prediction)
        except:
            steps_reward = 0
        reward += steps_reward

        # Zero reward if obviously wrong direction (e.g. spin)
        direction_diff = racing_direction_diff(
            optimals[0:2], optimals_second[0:2], [x, y], heading)
        if direction_diff > 30:
            reward = 1e-3
            
        # Zero reward of obviously too slow
        speed_diff_zero = optimals[2]-speed
        if speed_diff_zero > 0.5:
            reward = 1e-3
            
        ## Incentive for finishing the lap in less steps ##
        REWARD_FOR_FASTEST_TIME = 1500 # should be adapted to track length and other rewards
        STANDARD_TIME = 55  # seconds (time that is easily done by model)
        FASTEST_TIME = 52  # seconds (best time of 1st place on the track)
        if progress == 100:
            finish_reward = max(1e-3, (-REWARD_FOR_FASTEST_TIME /
                      (15*(STANDARD_TIME-FASTEST_TIME)))*(steps-STANDARD_TIME*15))
        else:
            finish_reward = 0
        reward += finish_reward
        
        ## Zero reward if off track ##
        if all_wheels_on_track == False:
            reward = 1e-3

        ####################### VERBOSE #######################
        
        if self.verbose == True:
            print("Closest index: %i" % closest_index)
            print("Distance to racing line: %f" % dist)
            print("=== Distance reward (w/out multiple): %f ===" % (distance_reward))
            print("Optimal speed: %f" % optimals[2])
            print("Speed difference: %f" % speed_diff)
            print("=== Speed reward (w/out multiple): %f ===" % speed_reward)
            print("Direction difference: %f" % direction_diff)
            print("Predicted time: %f" % projected_time)
            print("=== Steps reward: %f ===" % steps_reward)
            print("=== Finish reward: %f ===" % finish_reward)
            
        #################### RETURN REWARD ####################
        
        # Always return a float value
        return float(reward)


reward_object = Reward() # add parameter verbose=True to get noisy output for testing


def racingLine4(params):
    return reward_object.reward_function(params)