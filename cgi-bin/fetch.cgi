#!C:\xampp\perl\bin\perl.exe -wT

		#Incase of using Strawberry perl replace the above line to #!C:\Strawberry\perl\bin\perl.exe -wT
		#In Line replace the above line to #!/usr/bin/perl

use CGI;
use DBI;
my $dsn = "DBI:mysql:hotel";

my $dbh = DBI->connect($dsn, "root","") or die $DBI::errstr;

my $q = CGI->new;
my $query=CGI->new;
print $q->header();

my $roomno =$query->param('roomno');
my $sql = "SELECT * FROM users WHERE room_no=?";
  my $sth = $dbh->prepare($sql);
 
  # execute the query
  $sth->execute($roomno);

   my @row = $sth->fetchrow_array();

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
        <table align=center>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Room Number</th>
                <th>Contact</th>
                <th>Number of Persons</th>
            </tr>
            <tr>
                <td>@row[0]</td>
                <td>@row[1]</td>
                <td>@row[2]</td>
                <td>@row[3]</td>
                <td>@row[4]</td>
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
   $sth->finish();