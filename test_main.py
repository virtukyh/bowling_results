#!/usr/bin/env python2.7

import unittest, random, json

from os import listdir
from os.path import isfile, join, splitext

from main import bowling_scores

FIXTURES_PATH = './fixtures'


class TestBowlingScores(unittest.TestCase):
    
    def test_predefined_scores(self):
        """ Going through JSON fixtures from ./fixtures dir and compare 
        calculated scores with a scores constant from filename, where fixture
        filename is the right scores number, and fixture content it is a list
        of shots in a [x, x, x ...] format where x - integer.
        """
        json_scores = [
            f for f in listdir(FIXTURES_PATH) 
            if isfile(join(FIXTURES_PATH, f)) and f.endswith('.json')
        ]
        
        for score_fixture in json_scores:
            # Take the right scores from the filename
            fixture_scores = int(splitext(score_fixture)[0])
            
            with open(join(FIXTURES_PATH, score_fixture)) as data_file:    
                fixture_shots = json.load(data_file)
            
            # Calculate scores using our own method
            calculated_scores = bowling_scores(fixture_shots)
            
            print 'Shots: {}'.format(fixture_shots)
            print 'Scores: {}'.format(calculated_scores)
            
            self.assertEquals(calculated_scores, fixture_scores) 


if __name__ == '__main__':
    unittest.main()
