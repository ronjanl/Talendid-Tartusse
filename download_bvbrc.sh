for i in `cat genome_list`; 
do wget -qN "ftp://ftp.bvbrc.org/genomes/$i/$i.fna";
done;
