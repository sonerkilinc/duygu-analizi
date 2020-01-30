<?php
if(isset($_POST['shortcode'])){
	$shortcode = $_POST['shortcode'];
}

if(preg_match('/[\'^£$%&*()}{@#~?><>,|=+¬-]/',$shortcode)){
	echo "unsupported short code for post<br>";
	return;
}
$output = exec("/usr/bin/python3.5 sentiment/sa.py $shortcode");
echo $output."<br>";

?>
