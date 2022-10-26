CREATE TABLE EXAMS(ExNO smallint primary key,ExName varchar(20),ExDate date,ExCode varchar(15) unique not null);

insert into exams values
(1,"Pre Mid Term",'2021-12-20',"premidterm"),
(2,"Mid Term - 1",'2022-02-17',"midterm1"),
(3,'Quaterly','2022-03-20',"quaterly"),
(4,'Term - 1','2022-05-15',"term1"),
(5,'Mid Term - 2','2022-06-10',"midterm2"),
(6,'Mid Term - 3','2022-06-30',"midterm3"),
(7,'Revision - 1','2022-07-15',"revision1"),
(8,'Revision - 2','2022-08-05',"revision2"),
(9,'Revision - 3','2022-09-10',"revision3"),
(10,'Pre Boards-1','2022-10-20',"preboards1"),
(11,'Pre Boards-2','2022-11-25',"preboards2");