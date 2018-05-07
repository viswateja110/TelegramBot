<? php
require_once('dbconnection.php');
$uname=$_POST['uname'];
$pwd=$_POST['pasword'];
$sql="select * from users where email='$uname' and pasword='$pwd'";
$res=$conn->query($sql);
$count=mysqli_num_rows($res);
if($count==0){
    echo "invalid";
}else{
    echo "valid";
}
