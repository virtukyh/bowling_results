#!/usr/bin/env python2.7

from copy import copy

SHOT_STRIKE = 10
SHOT_FRAMES = 10

shots_testing_data = [
    10, 
    3, 7, 
    6, 1, 
    10, 
    10, 
    10, 
    2, 8, 
    9, 0, 
    7, 3, 
    10,
    10, 10
]


def bowling_scores(shots_data):
    """ Calculate bowling scores result, taking shots data as input argument
    as a list of integers.
    """
    
    # We need to copy here because we are using that function in a way where
    # we are modifying mutable object passed as arg, AND return a different
    # value as function result - without copy we will get our arg changed
    shots = copy(shots_data)
    
    total_scores = 0
    
    for frame_number in range(1, SHOT_FRAMES + 1):
        if not len(shots):
            raise ValueError('Shots count do not match frames number')
            
        shot = shots.pop(0)
        
        if shot == SHOT_STRIKE:
            # General strike counting rules
            # scores = shot[n] + shot[n+1] + shot[n+2] (next two shots)
            # where n - current shot index
            if frame_number < SHOT_FRAMES:
                # Strike not from the last frame
                total_scores += shot + shots[0] + shots[1]
            else:
                # Strike from the last frame
                total_scores += shot + shots.pop(0) + shots.pop(0)
                
        elif shot < SHOT_STRIKE:
            if shot + shots[0] == SHOT_STRIKE:
                # Spare shot counting rules:
                # scores = (shot[n] + shot[n+1]) + shot[n+2]
                total_scores += (shot + shots.pop(0)) + shots[0]
            else:
                # Just a general shot
                total_scores += shot + shots.pop(0)
    
    return total_scores


if __name__ == "__main__":
    scores = bowling_scores(shots_testing_data)
    print 'Shots line: {}'.format(shots_testing_data)
    print 'Scores: {}'.format(scores)
