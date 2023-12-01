#! /usr/bin/perl -w
my @files = glob ("/mambakodu/alice/resistentsed_kataloog/*.fna");
foreach my $f (@files){
	my @tmp = split(/\./,$f);
	my $id = $tmp[1];
#	system("head -n 1 $f");
	system ("perl seeker.pl -d /storage9/db/strainseeker_db/ss_db_w16_MLST/ -i $f -o $id.w16.ssreport");
}

@files = glob ("/mambakodu/elisavet/susceptible/*.fna");
foreach my $f (@files){
        my @tmp = split(/\./,$f);
        my $id = $tmp[1];
       	system ("perl seeker.pl -d /storage9/db/strainseeker_db/ss_db_w16_MLST/ -i $f -o $id.w16.ssreport");
}
