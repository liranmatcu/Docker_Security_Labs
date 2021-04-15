<?php

$servername = "xss-demo-database:3306";
$username = "xss_db_user";
$password = "password1234";
$dbname = "xss_db";

$mysqli = new mysqli($servername, $username, $password, $dbname);

if ($mysqli->connect_error) {
    die("Connection to database failed: " . $mysqli->connect_error);
}
?>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Adorable dog lovers</title>
    <style>
      body {
        font-family: sans-serif;
      }
      .content {
        margin: 0px auto;
        width: 100%;
        max-width: 600px;
        text-align: center;
      }
      .dog_img {
        width: 100%;
      }
      hr {
        margin: 30px 0;
      }

      .comments_wrap {
        text-align: left;
      }
      .comment {
        display: grid;
        grid-template-columns: 0fr 1fr;
        grid-template-rows: repeat(2, 1fr);
        grid-column-gap: 25px;
        grid-row-gap: 5px; 
        margin-bottom: 20px;
        
      }
      .comment .avatar {
        width: 70px;
        height: 70px;
        grid-column: 1;
        grid-row: 1 / span 2;
        border-radius: 50%;
        place-self: center;
      }
      .comment .name {
        grid-column: 2;
        grid-row: 1;
        align-self: end;
        font-weight: bold;
      }
      .comment .text {
        grid-column: 2;
        grid-row: 2;
        align-self: start;
      }

      .add_comment {
        text-align: left;
        width: 100%;
        max-width: 400px;
        margin: 0 auto;
      }

      .add_comment input, .add_comment textarea, .add_comment button {
        box-sizing: border-box;
        width: 100%;
        margin: 8px 0;
      }
      .add_comment input, .add_comment textarea {
        padding: 8px;
      }
    </style>
  </head>
  <body>
  <div class="content">
  <h1>❗❗ IMPORTANT ❗❗</h1>
  <h2>I found a cute picture of a dog! Please add your comments. </h2>

  <img src="assets/dog.jpg" alt="dog" class="dog_img"/>

  <br/>
  <hr/>
  <div class="comments_wrap">
    <h3>Comments</h3>

    <?php

    $result = $mysqli->query("SELECT username, comment FROM comments");

    if ($result->num_rows > 0) {

      while($row = $result->fetch_assoc()) {
        echo '<div class="comment"><img src="assets/avatar.jpg" class="avatar"/>';
        echo '<span class="name">' . $row["username"] . ":</span>";
        echo '<span class="text">' . $row["comment"] . "</span></div>";
    }
    } else {
      echo "There are no comments.</br>";
    }

    ?>
  </div>
  <hr/>
  <div class="add_comment">
    <h4>Add a comment</h4>
    <form action="add_comment.php" method="post">
    <input type="text" name="username" placeholder="Your name" required/>
    <textarea name="comment" placeholder="Your comment" required></textarea>
    <button type="submit">Add comment</div>
    </form>
  </div>
  </div>
  </body>
</html>

<?php  $mysqli->close(); ?>