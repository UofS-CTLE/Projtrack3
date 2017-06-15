$files = Get-ChildItem ctleweb\projtrack\templates\projtrack
$strings = @{"/projtrack3/" = "projtrack:index"; 
			 "/projtrack3/home/" = "projtrack:home";
			 "/projtrack3/all_projects/" = "projtrack3:all_projects/";
			 "/projtrack3/my_projects/" = "projtrack3:my_projects/";
			 "/projtrack3/add_project/" = "projtrack3:add_project/";
			 "/projtrack3/add_client/" = "projtrack3:add_client";
			 "/projtrack3/add_department/" = "projtrack3:add_department";
			 "/projtrack3/client_view/" = "projtrack3:client_view";
			 "/projtrack3/report_page/" = "projtrack3:report_page"}

for ($i = 0; $i -lt $files.Count; $i++) {
	$strings.GetEnumerator() | % {
		$content = Get-Content($files[$i])
		$content = $content.replace($_.key, $_.value[$_.key])
		$content | out-file $files[$i]
	}
}