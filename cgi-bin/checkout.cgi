#!C:\xampp\perl\bin\perl.exe -wT

		#Incase of using Strawberry perl replace the above line to #!C:\Strawberry\perl\bin\perl.exe -wT
		#In Line replace the above line to #!/usr/bin/perl

use CGI;
use DBI;
my $dsn = "DBI:mysql:hotel";

my $dbh = DBI->connect($dsn, "root","") or die $DBI::errstr;

my $q = CGI->new;
my $query=CGI->new;
print $q->header;

my $roomno =$query->param('roomno');

  my $sth = $dbh->prepare("UPDATE rooms SET full=NULL WHERE full=?");
  $sth->execute($roomno);

  $sth = $dbh->prepare("INSERT INTO rooms(available) VALUES (?)");
  $sth->execute($roomno);  

  $sth = $dbh->prepare("DELETE FROM users WHERE room_no=?");
  $sth->execute($roomno);

  $sth = $dbh->prepare("DELETE FROM rooms WHERE available IS NULL and full IS NULL");
  $sth->execute();

    print "<html>
			<head>
			<style>
			h2{
				color:#0C97FA;
				font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
				margin-top:20vh;
			}
			</style>
			</head>
			<body>
			<center>
			<h2>Checkout Successful... Redirecting to Dashboard...!</h2>
			</center>
			</body>
  			</html>";
    my $url = "/perl/dashboard.html";
    my $t=2;
    print "<META HTTP-EQUIV=refresh CONTENT=\"$t;URL=$url\">\n";

  $sth->finish();