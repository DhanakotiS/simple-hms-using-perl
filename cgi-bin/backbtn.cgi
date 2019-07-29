#!C:\xampp\perl\bin\perl.exe -wT

		#Incase of using Strawberry perl replace the above line to #!C:\Strawberry\perl\bin\perl.exe -wT
		#In Line replace the above line to #!/usr/bin/perl

use CGI;
use DBI;

use strict;
use warnings;

my $q = CGI->new;
my $query=CGI->new;
print $q->header;


my $url = "/perl/dashboard.html";
my $t=0;
print "<META HTTP-EQUIV=refresh CONTENT=\"$t;URL=$url\">\n";