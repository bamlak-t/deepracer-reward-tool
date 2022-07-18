'''
    Contains multiple reward functions to be checked
'''

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