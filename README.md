Convert SVG to CDF
==================

I had a dilemma. I needed a CDF, no one had the data, and someone sent me a graphical CDF embedded in PDF and EPS. I needed to convert this graph into a tabulated CDF. There
are two problems with this
-   One needs points from the CDF
-   One needs to convert from points to CDFs

The current toolchain is

1. Open the PDF (of the entire paper, for example) or EPS in Illustrator (or Inkscape)
2. Delete all objects (including the axes) except the curve itself
3. Save as a new SVG file
4. Run svg-parser.py to get a set of points.
5. Run points-to-cdf.py to get the CDF. Refer back to the original graph to
   get the following parameters:
    - xmin: the x value of the left-most point
    - xmax: the x value of the right-most point
    - ymin: the y value of the left-most point
    - ymax: the y value of the right-most point

To convert log-linear CDFs use points-to-cdf-log.py. You will need one
additional parameter:
    - base: the base of the logarithm (usually 10)
