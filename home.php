<!DOCTYPE html>
<html lang="en">
<head>
  <title>Database Querying</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js">
    $(document).ready(function(){
      $('#submit').click(function() {
        $.ajax({
          url: 'view_data.php',
          type: 'POST',
          /*
          data: {
              query-field: 'email@example.com',
              query-value: 'hello world!'
          },
          */
          data: 
          success: function(msg) {
              alert('Email Sent');
          }               
        });
      });
    });
  </script>

</head>
<body>

<div class="container-fluid">
  <h1>Query Database</h1>
  <p> Select entry field, and enter search</p> 

 <form action="view_data.php">
  <div class="form-group">
	  <label for="query-field">Query Field:</label>
	  <select class="form-control" id="query-field">
	    <option>Patient ID</option>
	    <option>Patient Last Name</option>
	    <option>Study Number</option>
	    <option>Media Name</option>
	  </select>
  </div>
  <div class="form-group">
    <label for="query-value">Query Value</label>
    <input type="text" class="form-control" id="query-value" placeholder = "Enter Query Value" required>
  </div>
  <button id = "submit" type="submit" class="btn btn-primary">Submit</button>
  </form>
</div>
<div class = "container-fluid">
<?php
$servername = "localhost";
$username = "fooiey";
$password = "Epic7ski";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
?>
</div>

<script>

</script>

</body>
</html>