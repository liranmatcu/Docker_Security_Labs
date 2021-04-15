<?php 
if (isset($_POST)) {

  $servername = "xss-demo-database:3306";
  $username = "xss_db_user";
  $password = "password1234";
  $dbname = "xss_db";


  if(!$_POST["username"]) die("No username given!");
  if(!$_POST["comment"]) die("No comment given!");

  $mysqli = new mysqli($servername, $username, $password, $dbname);

  if ($mysqli->connect_error) {
    die("Connection to database failed");
  }

  $stmt = $mysqli->prepare("INSERT INTO comments (username,comment) VALUES (?,?)");
  $stmt->bind_param('ss', $_POST["username"], $_POST["comment"]);
  $stmt->execute();

  header( "refresh:3;url=index.php" );
  echo "Your comment has been saved. Thanks! You will be redirected shortly. ";

  $stmt->close();
  $mysqli->close();
}else{
  echo ("You should not access this page directly");
}
?>