# Perception Challenge

## Answer

![](https://github.com/Willdwyer10/perception-challenge/blob/main/answer.png)

## Methodology

I used OpenCV for this task. First, I determined the area of the cones that we would be detecting,
so as to not detect objects too small (just noise) or too big. Then, I changed the thresholds for
the specific color we were detecting in order to mask off the cones. Once the cones were correctly
being identified, I had to draw lines that went through the cones. To do this, I used the basic
point-slope formula to calculate the points that the lines would have to be drawn from so as
to appear infinite (go off the screen), based on the locations of the boundary cones.

## What I tried, and why it didn't work

I used ChatGPT as my friend to learn the very basics of OpenCV, and it was a great resource to
learn about the specific functionality used during this task. The hardest part for me was
determining the correct HSV values to mask off the cones. I played with those values for a while
until the cones were correctly masked.

## Libraries

The main library was OpenCV, but Numpy was also used minutely.
