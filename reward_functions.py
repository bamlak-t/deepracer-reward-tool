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
    offTrack = params['is_off_track']
    
    if offTrack:
        reward = 1.0
    else:
        reward = 1e-3  

    return float(reward)