# all test cases passed

k = gets.to_i

k.times do
  puts "#{'*' * k}#{'x' * k}#{'*' * k}"
end

k.times do
  puts "#{' ' * k}#{'x' * k}#{'x' * k}"
end

k.times do
  puts "#{'*' * k}#{' ' * k}#{'*' * k}"
end