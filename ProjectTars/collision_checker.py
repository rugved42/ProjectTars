#!/usr/bin/env python3

import numpy as np
import scipy.spatial
from math import sin, cos, pi, sqrt

class obstacleChecker:
    def __init__(self, circle_offsets, circle_radii, weight):
        self._circle_offsets = circle_offsets
        self._circle_radii   = circle_radii
        self._weight         = weight

    def obstacle_check(self, paths, obstacles):
        """Returns a bool array on whether each path is obstacle free.

            obstacle_check_array: A list of boolean values which classifies
                whether the path is obstacle-free (true), or not (false).
        """
        obstacle_check_array = np.zeros(len(paths), dtype=bool)
        for i in range(len(paths)):
            obstacle_free = True
            path           = paths[i]

            # Iterate over the points in the path.
            for j in range(len(path[0])):
                
                circle_locations = np.zeros((len(self._circle_offsets), 2))
.
                circle_offset = np.array(self._circle_offsets)
                circle_locations[:, 0] = path[0][j] + circle_offset * cos(path[2][j])
                circle_locations[:, 1] = path[1][j] + circle_offset * sin(path[2][j])
                # --------------------------------------------------------------

                # Assumes each obstacle is approximated by a collection of
                # points of the form [x, y].
                # Here, we will iterate through the obstacle points, and check
                # if any of the obstacle points lies within any of our circles.
                # If so, then the path will collide with an obstacle and
                # the obstacle_free flag should be set to false for this flag
                for k in range(len(obstacles)):
                    obstacle_dists = \
                        scipy.spatial.distance.cdist(obstacles[k], 
                                                     circle_locations)
                    obstacle_dists = np.subtract(obstacle_dists, 
                                                  self._circle_radii)
                    obstacle_free = obstacle_free and \
                                     not np.any(obstacle_dists < 0)

                    if not obstacle_free:
                        break
                if not obstacle_free:
                    break

            obstacle_check_array[i] = obstacle_free

        return obstacle_check_array

    ######################################################
    ######################################################
    def select_best_path_index(self, paths, obstacle_check_array, goal_state):
        """Returns the path index which is best suited for the vehicle to
        traverse.
        """
        best_index = None
        best_score = float('Inf')
        for i in range(len(paths)):
            # Handle the case of obstacle-free paths.
            if obstacle_check_array[i]:

                score = np.sqrt((paths[i][0][-1]-goal_state[0])**2+(paths[i][1][-1]-goal_state[1])**2)
                # --------------------------------------------------------------

                # Compute the "proximity to other colliding paths" score and
                # add it to the "distance from centerline" score.
                # The exact choice of objective function is up to you.
                for j in range(len(paths)):
                    if j == i:
                        continue
                    else:
                        if not obstacle_check_array[j]:
                            
                            pass

            # Handle the case of colliding paths.
            else:
                score = float('Inf')
                
            # Set the best index to be the path index with the lowest score
            if score < best_score:
                best_score = score
                best_index = i

        return best_index
