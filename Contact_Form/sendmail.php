<?php
header("Content-Type:text/html; charset=utf-8");
include("class.phpmailer.php");
//include ("db/configure.php");
//include ("db/connect_db.php");

//$sql = "SELECT * from contacts";
//$rs = mysql_query($sql, $link);
$con = mysqli_connect('localhost', 'root', '1234567890', 'mycontact');
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$Name=mysql_escape_string($_POST['sndname']);
$Mail=mysql_escape_string($_POST['sendmail']);
$Subject=mysql_escape_string($_POST['subject']);
$Sendbody=mysql_escape_string($_POST['sendbody']);


$mail= new PHPMailer(); //建立新物件
$mail->IsSMTP(); //設定使用SMTP方式寄信
$mail->SMTPAuth = true; //設定SMTP需要驗證
$mail->SMTPSecure = "ssl"; // Gmail的SMTP主機需要使用SSL連線
$mail->Host = "smtp.gmail.com"; //Gamil的SMTP主機
$mail->Port = 465;  //Gamil的SMTP主機的埠號(Gmail為465)。
$mail->CharSet = "utf-8"; //郵件編碼
 
$mail->Username = ""; //Gamil帳號
$mail->Password = ""; //Gmail密碼
 
$mail->From = $Mail; //寄件者信箱
$mail->FromName = "線上客服"; //寄件者姓名
 
$mail->Subject ="一封線上客服信";  //郵件標題
$mail->Body = "姓名:".$Name."<br>信箱:".$Mail."<br>主題:".$Subject."<br>回應內容:".$Sendbody; //郵件內容
 
$mail->IsHTML(true); //郵件內容為html ( true || false)
$mail->AddAddress("aj1384@gcloud.ntpc.gov.tw"); //收件者郵件及名稱
 
if(!$mail->Send()) {
	echo "發送錯誤: " . $mail->ErrorInfo;
} else {

	mysqli_query($con,"INSERT INTO contacts (user_name, user_mail) VALUES ('".$Name."', '".$Mail."')");
    mysqli_close($con);
	echo "<div align=center>感謝您的回覆，我們將會盡速處理!</div>";
}

?>
