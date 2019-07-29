#!C:\xampp\perl\bin\perl.exe -wT

		#Incase of using Strawberry perl replace the above line to #!C:\Strawberry\perl\bin\perl.exe -wT
		#In Line replace the above line to #!/usr/bin/perl

use CGI;
use DBI;
my $dsn = "DBI:mysql:hotel";

my $dbh = DBI->connect($dsn, "root","") or die $DBI::errstr;

my $q = CGI->new;
my $query=CGI->new;

my $roomno =$query->param('roomno');

my $sql = "SELECT * FROM users;";
  my $sth = $dbh->prepare($sql);
  $sth->execute();

print $q->header();

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
      .ravailable{

         float: left;
         width: 40%;
         padding: 1.5vw;
         margin-top: 1vh;
         border-radius: 2vw;
         margin-left: 3vw;
         color: #FFFFFF;
      }
      .rfull{

         float:right;
         width:30%;
         padding: 1.5vw;
         margin-top: 1vh;
         border-radius: 2vw;
         margin-right: 3vw;
         color: #FFFFFF;
      }
      table{
         text-align: center;
         border: 2px solid rgba(0, 100, 172, 0.938);
         border-radius:1vh;
      }
      td,th{
         padding: 1vw;
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
      <form action=/cgi-bin/backbtn.cgi>
            <input type=submit value=Back>
         </form>
    ";
print $html;



    print "<div class=ravailable><h3 style=color:#005d9c;>Rooms Full</h3>
            <table width=600><tr id=heading>
                <th>ID</th>
                <th>Name</th>
                <th>Room Number</th>
                <th>Contact</th>
                <th>Number of Rooms</th>
            </tr>";
        
   while(my @row = $sth->fetchrow_array()){
       $rid= $row[0];
       $rname= $row[1];
       $rroom= $row[2];
       $rcontact= $row[3];
       $rnumber= $row[4];
       print "<tr>
                <td>$rid</td>
                <td>$rname</td>
                <td>$rroom</td>
                <td>$rcontact</td>
                <td>$rnumber</td>
            </tr>\n";
   }
   print"</table></div>";

    print "<div class=rfull>
    <h3 style=color:#005d9c;>Available</h3>
            <table width=300><tr id=heading>
                <th>Available rooms</th>
            </tr>";

   my $sql = "SELECT available FROM rooms WHERE available IS NOT NULL;";
   my $sth = $dbh->prepare($sql);
   $sth->execute();
        
   while(my @full = $sth->fetchrow_array()){
      my $val = $full[0];
       print "<tr><td>$val</td></tr>\n";
   }
   print"</table></div></body>
</html>";
   $sth->finish();