#!C:\xampp\perl\bin\perl.exe -wT

		#Incase of using Strawberry perl replace the above line to #!C:\Strawberry\perl\bin\perl.exe -wT
		#In Line replace the above line to #!/usr/bin/perl
        
use CGI;
use DBI;

my $q = CGI->new;
my $query=CGI->new;
my $uname = $query->param('uname');
my $pword = $query->param('pword');

my $dsn = "DBI:mysql:hotel";

my $dbh = DBI->connect($dsn, "root","") or die $DBI::errstr;

my $q = CGI->new;
my $query=CGI->new;
print $q->header();

my $sql = "SELECT * FROM admin WHERE aname=?";
my $sth = $dbh->prepare($sql);
$sth->execute($uname);

my @row = $sth->fetchrow_array();

my $admin = $row[0];
my $pass = $row[1];

if($uname eq $admin && $pword eq $pass)
{
    my $url = "/perl/dashboard.html";
    my $t=0;
    print "<META HTTP-EQUIV=refresh CONTENT=\"$t;URL=$url\">\n";
}
else
{
    print "Username or Password is Incorrect...Please Try again!";
    my $url = "/perl/";
    my $t=2;
    print "<META HTTP-EQUIV=refresh CONTENT=\"$t;URL=$url\">\n";
}