require 'rake/testtask'

Rake::TestTask.new do |t|
  t.libs.push('.')
  t.test_files = FileList['test/*_spec.rb']
  t.verbose = true
end
