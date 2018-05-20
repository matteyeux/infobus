create database ratp;
use ratp;

create table parcours2(
numpar char(5) not null,
numpt char(5) not null,
lati decimal(11,6),
longi decimal(11,6),
alt decimal(4),
nompt char(20),
despt char(35)
);
