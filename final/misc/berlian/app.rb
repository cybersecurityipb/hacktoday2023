#!/usr/bin/env ruby

Dir.glob("*.txt").each do |file|
  next if file == "flag.txt"
  File.rename(file, "flag.txt")
end

flag = "flag.txt"

timestamp = Time.now.to_i.to_s
salted = `echo "#{timestamp}" | cat "#{flag}" - | md5sum | awk '{ print $1 }'`.chomp
newflag = "#{salted}.#{File.basename(flag).split(".").last}"

File.rename(flag, newflag)

banned_commands = ["ls", "cd", "pwd", "rm", "cp", "mv", "xxd", "less"]
banned_keywords = ["sh"]
banned_symbols = ["$", "[", "]", "*", "!", "{", "}", "|", "/", "a", "i", "u", "o", "A", "I", "U", "O"]

loop do
  print 'sepuh@hacker:~$ '
  exp = gets.chomp

  if banned_commands.any? { |command| exp.include?(command) } ||
     banned_keywords.any? { |keyword| exp.match(/#{keyword}/i) } ||
     banned_symbols.any? { |symbol| exp.include?(symbol) }
    puts "Ampun Puh :("
    exit(1)
  end

  res = eval(exp, TOPLEVEL_BINDING)
  puts res
end
