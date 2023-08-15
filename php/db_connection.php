<?php
// Check if the login form is submitted
if (isset($_POST['login'])) {
  // Replace the following lines with your database connection logic
  $db_host = 'localhost';
  $db_username = 'raven';
  $db_password = 'Penis';
  $db_name = 'raven_login';

  // Create a database connection
  $conn = mysqli_connect($db_host, $db_username, $db_password, $db_name);

  if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
  }

  // Sanitize user inputs to prevent SQL injection
  $username = mysqli_real_escape_string($conn, $_POST['username']);
  $password = mysqli_real_escape_string($conn, $_POST['password']);

  // Perform user authentication
  $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
  $result = mysqli_query($conn, $sql);

  if (mysqli_num_rows($result) === 1) {
    // User is authenticated, redirect to a dashboard or protected page
    header("Location: test1.html");
    exit();
  } else {
    // Invalid credentials, redirect back to the login page with an error message
    header("Location: index.html?error=1");
    exit();
  }

  // Close the database connection
  mysqli_close($conn);
}
?>