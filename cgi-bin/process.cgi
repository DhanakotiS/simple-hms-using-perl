#!C:\xampp\perl\bin\perl.exe -wT

		#Incase of using Strawberry perl replace the above line to #!C:\Strawberry\perl\bin\perl.exe -wT
		#In Line replace the above line to #!/usr/bin/perl

use CGI;
use DBI;

use strict;
use warnings;


my $dsn = "DBI:mysql:hotel";  #Replace hotel with database name

my $dbh = DBI->connect($dsn, "root","") or die $DBI::errstr;

my $q = CGI->new;
my $query=CGI->new;
my $name=$query->param('name');
my $room_no=$query->param('roomno');
my $mobile=$query->param('mobile');
my $persons=$query->param('persons');

my $sth = $dbh->prepare("INSERT INTO users(name,room_no, mobile, persons) VALUES(?,?,?,?);");

$sth -> execute($name,$room_no,$mobile,$persons);
  my $sth = $dbh->prepare("UPDATE rooms SET available=NULL WHERE available=?");
  $sth->execute($room_no);

  my $sth = $dbh->prepare("INSERT INTO rooms(full) VALUES (?)");
  $sth->execute($room_no);

  my $sth = $dbh->prepare("DELETE FROM rooms WHERE available IS NULL and full IS NULL;");
  $sth->execute();
  
print $q -> CGI::header('text/html');
my $html ="
   <html>
   <head>
   <style>
      body{
         background-color: #EBEBEB;
         font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
      }
      h1{
			background: -webkit-linear-gradient(rgb(2, 247, 255),rgb(0, 53, 228));
			-webkit-background-clip: text;
			-webkit-text-fill-color: transparent;
			font-size: 3vw;
			margin-left: 40vw;
         margin-top: 2vw;
		}
      table{
         background-image: linear-gradient(to bottom right,#0C97FA,#16E1F5);
         box-shadow: 2vh 2vh 6vh 0.2vh rgba(12, 151, 250, 0.747);
         padding: 2vw;
         margin-top: 20vh;
         border-radius: 2vw;
         border: 1px solid rgba(12, 151, 250, 0.747);
         color: #FFFFFF;
         text-align:center;
      }
      td,th{
         border: 2px solid rgba(0, 100, 172, 0.938);
         padding: 1vw;
         border-radius: 5px;
      }
      form input{
         width: 10vw;
			border-radius: 1vw;
			background-color: #2fc2df;
         padding: 1vw;
         margin-top: 1vw;
      }
   </style>
   </head>
    <body>
      <h1>HOTEL MANAGEMENT SYSTEM</h1>
      <h3 style=color:#0C97FA;text-align:center;>Room Allocated Successfully...!</h3>
        <table align=center>
            <tr>
                <th>Name</th>
                <th>Room Number</th>
                <th>Contact</th>
                <th>Number of Rooms</th>
            </tr>
            <tr>
                <td>$name</td>
                <td>$room_no</td>
                <td>$mobile</td>
                <td>$persons</td>
            </tr>
        </table>
        <center>
        <form action=/cgi-bin/backbtn.cgi>
         <input type=submit value=Back>
        </form>
        </center>
    </body>
</html>";
print $html;