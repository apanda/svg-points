#!/usr/bin/env ruby

# Method: treat the CDF like a sideways histogram, and compute the average across
# all buckets.

weighted_sum = 0.0
# previous_y is used to compute how wide the current bucket is
previous_y = 0.0

File.foreach(ARGV.shift) do |line|
  x, y = line.chomp.split(",").map { |x| x.to_f }
  delta_y = y - previous_y
  # Width * Heigth
  weighted_sum += delta_y * x
  previous_y = y
end
puts "Mean: #{weighted_sum}"
