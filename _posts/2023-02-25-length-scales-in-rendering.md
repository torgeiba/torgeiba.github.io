# Length Scales In Rendering

Usually in rendering we consider spatial scale to be somewhat arbitrary, i.e we only deal with coordinates, and whether we use meters or centimeters as
a base unit for our measurement is mostly irrelevant as long as we are consistent and use coordinates that are a reasonable fit for the content we wish to render.

But it is still interesting to consider the appropriate scale to use for rendering.
Here are some potentially relevant sizes for reference:

- Human hair diameter: 0.06 mm
- Grain of sand: 0.06 to 2.0 mm
- Pixel distance on a 4K PC monitor: 0.18 mm
- Size of a human pupil: 2-9 mm
- Diameter of a human eye: About 2.5 cm.
- Interpupillary distance: About 6 cm
- Viewing distance from PC monitor: about 60 cm
- Size of a large PC monitor : 70 cm wide, 40 cm high
- Average human height: About 1.7m
- Size length of typical countries if they were flat and square shaped: 100 to 3000 km
- Radius of the earth: 6371 km

So the smallest and largest sizes listed here in the same units (meters) for comparison
- 0.00006
- 6000000.0

The scale difference is about $10^12$ or approximately $2^40$. The geometric mean is about 5.5 meters.

for an arena shooter style game you may only care about objects within at most a kilometer radius, in which case we may choose 1000 and 0.001 meters as our range,
for which the geometric mean is exactly 1 meter.

According to the internet:
> Humans can at best resolve two lines about 0.01 degrees apart: a 0.026 mm gap, 15cm the eyes.
> Typically objects 0.04mm wide, the width of a fine human hair, are just distinguishable by good eyes, objects 0.02mm wide are not.

From performing a quick and simple test of displaying a single white pixel on a black background on a 4k resolution 32 inch monitor (0.18 mm pixel distance),
the pixel can clearly be seen at a distance of several meters.

