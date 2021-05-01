<h1>Welcome to the Demo</h1>

<?php 
function submit() {
    $host = 'mysql';
    $user = 'root';
    $pass = 'password';
    $dbname = 'injectionAttack';
    $conn = new mysqli($host, $user, $pass, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 

    $product = $_POST['product'];

    #removes the last extra space/spaces in user input
    // $product = rtrim($product);
    
    #used for removing characters used for sql injection
    // $product = str_replace(array("(", ")" , ";" , "--"), '', $product);

    $sql = "SELECT id, product_name, product_type, description, price  FROM products WHERE product_name LIKE '%$product%'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "<table><tr><th>ID</th><th>Name</th><th>Type</th><th>Description</th><th>Price</th></tr>";
        // output data of each row
        while($row = $result->fetch_assoc()) {
        echo "<tr><td>".$row["id"]."</td><td>".$row["product_name"]."</td><td>".$row["product_type"]."</td><td>".$row["description"]."</td><td>".$row["price"]."</td></tr>";
        }
        echo "</table>";
    } else {
        echo "0 results";
    }
    $conn->close();
}
if(array_key_exists('submit', $_POST)) {
    submit();
}
?>

<form method="post">
    <input type="text" id="product" name="product">
    <input type="submit" value="Submit" name="submit">
</form>