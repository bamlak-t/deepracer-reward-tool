class Params:

    def __init__(self):
    
        self.all_wheels_on_track = True        # flag to indicate if the agent is on the track
        self.is_reversed = False               # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
        self.speed = 1,                        # agent's speed in meters per second (m/s)
        self.steering_angle = 15               # agent's steering angle in degrees
        self.heading= 30                       # agent's yaw in degrees


    def setX(self, x):
        self.x = x

    def sety(self, y):
        self.y = y
    
    def setClosestWaypoints(self, closest_waypoints):
        self.closest_waypoints = closest_waypoints

    def setDistanceFromCenter(self, distance_from_center):
        self.distance_from_center = distance_from_center

    def setIsLeftOfCenter(self, is_left_of_center):
        self.is_left_of_center = is_left_of_center
    
    def setIsOffTrack(self, is_offtrack):
        self.is_offtrack = is_offtrack
    
    def setProgress(self, progress):
        self.progress = progress
    
    def setSteps(self, steps):
        self.steps = steps

    def setTrackLength(self, track_length):
        self.track_length = track_length
    
    def setTrackWidth(self, track_width):
        self.track_width = track_width
    
    def setWaypoints(self, waypoints):
        self.waypoints = waypoints

    def getx(self):
        return self.x
    
    def gety(self):
        return self.y
    
    def getClosestWaypoints(self):
        return self.closest_waypoints
    
    def getDistanceFromCenter(self):
        return self.distance_from_center
    
    def getIsLeftOfCenter(self):
        return self.is_left_of_center
    
    def getIsOffTrack(self):
        return self.is_offtrack
    
    def getProgress(self):
        return self.progress
    
    def getSteps(self):
        return self.steps
    
    def getTrackLength(self):
        return self.track_length

    def getTrackWidth(self):
        return self.track_width
    
    def getWaypoints(self):
        return self.waypoints
    
    def getAllWheelsOnTrack(self):
        return self.all_wheels_on_track
    
    def getIsReversed(self):
        return self.is_reversed
    
    def getSpeed(self):
        return self.speed
    
    def getSteeringAngle(self):
        return self.steering_angle
    
    def getHeading(self):
        return self.heading

    def getAll(self):
        return {
        "all_wheels_on_track": self.all_wheels_on_track,   
        "track_length": self.track_length,                  
        "track_width": self.track_width,                  
        "is_reversed": self.is_reversed,                 
        "waypoints": self.waypoints,       
        "speed": self.speed,                       
        "steering_angle": self.steering_angle,            
        "heading": self.heading,                  
        "x": self.x,                         
        "y": self.y,                          
        "closest_waypoints": self.closest_waypoints,     
        "distance_from_center": self.distance_from_center,        
        "is_left_of_center": self.is_left_of_center,           
        "is_offtrack": self.is_offtrack,                   
        "progress": self.progress,                    
        "steps": self.steps,                          
    }

        #  "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
        #  "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
        #  "objects_left_of_center": [bool, ],    # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
        #  "objects_location": [(float, float),], # list of object locations [(x,y), ...].
        #  "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
        #  "is_crashed": bool,                    # Boolean flag to indicate whether the agent has crashed.
        #  "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
