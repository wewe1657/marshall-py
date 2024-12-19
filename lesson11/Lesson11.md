# Lesson 11

## Quadrant Selection (CCC 2017 J1)

__YouTube Link:__ [https://www.youtube.com/watch?v=mPHv1YZXJ9o](https://www.youtube.com/watch?v=mPHv1YZXJ9o)

In this lesson, we are learning how to solve the [Quadrant Selection question](https://dmoj.ca/problem/ccc17j1).

A cartesian plane can be divided into 4 quadrants based on this image:

![quadrants](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4a4xLspgRHPa5dCoG6i8kO_SZsLVyWG90Sw&s)

A single point on a cartesian plane is composed of two values (x-coordinate, y-coordinate).

If the x-value is positive, the point can only be in either 1 or 4 quadrant.
If the y-value is positive, the point can only be in either 1 or 2 quadrant.

By combining the signs of both coordinates, we can determine where the point lies.

### Problem Overview

Given a single input containing a x-coordinate and a y-coodinate, determine which quadrant the value falls under.

### You will learn:

- How to use ```.split()``` method to create a list from a string
- How to use ```map()``` function to help us turn values in a list to integers
- How to use variable unpacking