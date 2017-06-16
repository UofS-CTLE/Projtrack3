use strict;
use warnings;

use Path::Tiny qw(path);

my $filename = $ARGV[0];
my $file = path($filename);

my $data = $file->slurp_utf8;
$data =~ s/\/projtrack3\/home\//{% url 'projtrack:home' %}/g;
$data =~ s/\/projtrack3\/all_projects\//{% url 'projtrack:all_projects' %}/g;
$data =~ s/\/projtrack3\/my_projects\//{% url 'projtrack:my_projects' %}/g;
$data =~ s/\/projtrack3\/add_project\//{% url 'projtrack:add_project' %}/g;
$data =~ s/\/projtrack3\/add_client\//{% url 'projtrack:add_client' %}/g;
$data =~ s/\/projtrack3\/add_department\//{% url 'projtrack:add_department' %}/g;
$data =~ s/\/projtrack3\/client_view\//{% url 'projtrack:client_view' %}/g;
$data =~ s/\/projtrack3\/report_page\//{% url 'projtrack:report_page' %}/g;
$data =~ s/\/projtrack3\/logout\//{% url 'projtrack:logout' %}/g;
$data =~ s/\/projtrack3\/project_edit\//{% url 'projtrack:edit_project' o.id %}/g;
$data =~ s/\/projtrack3\//{% url 'projtrack:index' %}/g;
$data =~ s/\/projtrack:index\//{% url 'projtrack:index' %}/g;
$file->spew_utf8($data);
