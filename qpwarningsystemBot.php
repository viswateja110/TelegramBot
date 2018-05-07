<?php
$token='telegram bot token';
$url='https://api.telegram.org/bot'.$token;
$x=100;
while($x>0){
    $updates=file_get_contents($url.'/sendmessage?chat_id=-262524743&text=box_is_opened');
    $x--;
}


print_r  ($updates);




?>
