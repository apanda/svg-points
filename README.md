Convert SVG to CDF
==================

I had a dilemma. I needed a CDF, no one had the data, and someone sent me a CDF in both PDF and EPS. I needed this graph into a CDF. There
are two problems with this
-   One needs points from the CDF
-   One needs to convert from points to CDFs

The current toolchain is

1. Open PDF or EPS in Illustrator (or Inkscape)
2. Copy the actual curve into a new file.
3. Save as SVG
4. Run svg-parser.py to get a set of points.
5. Run points-to-cdf.py to get the CDF.

This currently doesn't really do anything about logscales, but that is pretty easy to solve (this will be updated shortly).
