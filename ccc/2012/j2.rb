# all test cases passed

a = gets.to_i
b = gets.to_i
c = gets.to_i
d = gets.to_i

if a == b && a == c && a == d
  puts "Fish At Constant Depth"
elsif a < b && b < c && c < d
  puts "Fish Rising"
elsif a > b && b > c && c > d
  puts "Fish Diving"
else
  puts "No Fish"
end