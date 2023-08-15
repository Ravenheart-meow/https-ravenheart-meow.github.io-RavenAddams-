<?php
// Start the session
session_start();

// Include the database connection file
require_once 'db_connection.php';

// Check if the login form is submitted
if (isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Prepare the SQL statement to fetch the hashed password from the database
    $sql = "SELECT password FROM users WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->bind_result($hashedPassword);
    $stmt->fetch();
    $stmt->close();

    // Verify the entered password against the hashed password
    if (password_verify($password, $hashedPassword)) {
        // Password is correct, set the session variable
        $_SESSION['authenticated'] = true;
        header("Location: dashboard.php");
        exit();
    } else {
        // Invalid credentials, redirect back to the login page with an error message
        header("Location: login.html?error=1");
        exit();
    }
}
?>



