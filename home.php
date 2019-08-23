<!DOCTYPE html>
<html lang="en">
<head>
  <title>Database Querying</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  <style type = "text/css">
    table{
      border: 1px solid black;
    }
    tr{
      border-bottom: 1px solid black;
    }
    td{
      border-right: 1px solid black;
      border-left: 1px solid black;
    }
  </style>

</head>
<body>

<div class="container-fluid">
  <h1>Query Database</h1>
  <p> Select entry field, and enter search</p> 

 <form method = $_GET>
  <div class="form-group">
	  <label for="query-field">Query Field:</label>
	  <select class="form-control" id="query-field" name = "query-field">
	    <option>Patient ID</option>
	    <option>Patient Last Name</option>
	    <option>Study Number</option>
	    <option>Media Name</option>
	  </select>
  </div>
  <div class="form-group">
    <label for="query-value">Query Value</label>
    <input type="text" class="form-control" id="query-value" name = "query-value" placeholder = "Enter Query Value" required>
  </div>
  <button id = "submit" type="submit" class="btn btn-primary">Submit</button>
  </form>
</div>
<div class= "container-fluid">

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
echo "Connected successfully</br>";
/* shows available databases
$result = mysqli_query($conn,"SHOW DATABASES"); while ($row = 
mysqli_fetch_array($result)) { echo $row[0]."<br>"; }
*/
mysqli_select_db($conn, "mydatabase"); #either use this or in query say mydatabase.arch_study
#cant use mysqli and mysql at same time

if (!array_key_exists("query-field", $_GET)){
  exit();
}

if ($_GET["query-field"] == "Patient ID"){
  $patient_query_1 = "
    SELECT study_id, studycompleted_date, media_label
    FROM arch_study
    WHERE patient_id = {$_GET["query-value"]}";
  $patient_query_2 = "
    SELECT first_name, last_name, middle_init
    FROM arch_patient
    WHERE patient_id = {$_GET["query-value"]}";
  $result1 = $conn->query($patient_query_1);
  $result2 = $conn->query($patient_query_2);
  $total_studies = mysqli_num_rows($result1);
}
//https://stackoverflow.com/questions/21102124/mysql-error-unknown-column-in-where-clause answer by musa
if ($_GET["query-field"] == "Patient Last Name"){
  $last_name_query = "
    SELECT *
    FROM
    (SELECT patient_id
    FROM arch_patient
    WHERE last_name = '{$_GET["query-value"]}') AS A
    JOIN
    (SELECT study_id, studycompleted_date, media_label, patient_id
    FROM arch_study) AS B
    ON A.patient_id = B.patient_id";
    $result = $conn->query($last_name_query);
}
if ($_GET["query-field"] == "Study Number"){
  $study_number_query = "
    SELECT *
    FROM
    (SELECT patient_id, media_label, studycompleted_date, study_id
    FROM arch_study
    WHERE study_id = {$_GET["query-value"]}) AS A
    JOIN
    (SELECT volume_no, description, study_id
    FROM arch_media_detail
    WHERE study_id = {$_GET["query-value"]}) AS B
    ON A.study_id = B.study_id";
    $result3 = $conn->query($study_number_query);
}
/*
if ($_GET["query-field"] == "Media Name"){
  
}
*/
/*
if (!$result3) {
    trigger_error('Invalid query: ' . $conn->error);
}
*/


//output code (table format will be different for each type:
if ($_GET["query-field"] == "Patient ID"){
  $result2 = $result2->fetch_assoc();
  echo "patient name: ${result2["first_name"]} ${result2["middle_init"]} ${result2["last_name"]}</br>";
  echo "number of studies: ${total_studies}</br>";
  echo "<table>";
  if ($result1->num_rows > 0) {
      // output data of each row
      while($row = $result1->fetch_assoc()) {
          echo '<tr><td><a href ="http://localhost/home.php?query-field=Study+Number&query-value='.$row["study_id"].'">study_id: ' . $row["study_id"]. '</td><td> Date: ' . $row["studycompleted_date"]. ' </td><td>media_label ' . $row["media_label"]. '</td><tr>';
      }
      echo "</table>";
  } else {
      echo "0 results";
  }
}

if ($_GET["query-field"] == "Patient Last Name"){
  if ($result->num_rows > 0) {
      // output data of each row
    echo "<table>";
      while($row = $result->fetch_assoc()) {
          echo "<tr><td>patient_id: ".$row["patient_id"].'</td><td><a href ="http://localhost/home.php?query-field=Study+Number&query-value='.$row["study_id"].'">study_id: ' . $row["study_id"]. "</td><td> media_label: " . $row["media_label"]. "</td><td> Date: " . $row["studycompleted_date"]. "</td><td> media_label " . $row["media_label"]. "</td></tr>";
      }
      echo"</table>";
  } else {
      echo "0 results";
  }
}

if ($_GET["query-field"] == "Study Number"){
  if ($result3->num_rows > 0) {
      // output data of each row
      echo "<table>";
      while($row = $result3->fetch_assoc()) {
          echo "<tr><td>patient_id: ".$row["patient_id"]. "</td><td> Date: " . $row["studycompleted_date"]. "</td><td> media_label " . $row["media_label"]. "</td><td> volume_no: ".$row["volume_no"]. " </td><td> esc:".$row["description"]."</td></tr>";
      }
      echo "</table>";
  } else {
      echo "0 results";
  }
}

if ($_GET["query-field"] == "Media Name"){

}
?>
</div>

</body>
</html>