#!/usr/bin/env ruby

$stdout.sync = true

txt_files = Dir.glob("*.txt")
flag = txt_files.first

timestamp = Time.now.to_i.to_s
salted = `echo "#{timestamp}" | md5sum | awk '{ print $1 }'`.chomp
newflag = "#{salted}.#{File.basename(flag).split(".").last}"

File.rename(flag, newflag)

banned_commands = ["ls", "cd", "pwd", "rm", "cp", "mv", "xxd", "less"]
banned_keywords = ["sh"]
banned_symbols = ["$", "[", "]", "*", "!", "{", "}", "|", "/", "a", "i", "u", "o", "A", "I", "U", "O"]

loop do
  print 'sepuh@hacker:~$ '
  exp = gets
  exp ||= ''
  exp.chomp!

  if banned_commands.any? { |command| exp.include?(command) } ||
     banned_keywords.any? { |keyword| exp.match(/#{keyword}/i) } ||
     banned_symbols.any? { |symbol| exp.include?(symbol) }
    puts "Ampun Puh :("
    exit(1)
  end

  res = eval(exp, TOPLEVEL_BINDING)
  puts res
end
