# all test cases passed

print "Enter the speed limit: "
limit = gets.to_i
print "Enter the recorded speed of the car: "
speed = gets.to_i

if speed <= limit
  puts "Congratulations, you are within the speed limit!"
elsif speed <= (limit + 20)
  puts "You are speeding and your fine is $100."
elsif speed <= (limit + 30)
  puts "You are speeding and your fine is $270."
else
  puts "You are speeding and your fine is $500."
end