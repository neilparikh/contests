# all test cases passed

k = gets.to_i
word = gets.chomp
final = []
letters = [*'A'..'Z']

word.split('').each_with_index do |c, i|
  s = k + (i+1) * 3
  a = letters.index(c) - s
  while a < 0
    a += 26
  end
  final << letters[a]
end

puts final.join