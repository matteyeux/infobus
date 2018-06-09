create database ratp;
use ratp;

create table parcours2(
numpar char(25) not null,
numpt char(52) not null,
lati decimal(11,6),
longi decimal(11,6),
alt decimal(4),
nompt char(50),
despt char(35)
);
