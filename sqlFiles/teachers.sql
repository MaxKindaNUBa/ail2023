CREATE TABLE teachers(
TeacherID tinyint primary key,
UserID varchar(50) not null unique,
Pass varchar(20) not null unique,
MailID varchar(50) default 'N/A',
Class char(4) not null,
UniqueID mediumint not null);


insert into teachers (TeacherID, UserID, Pass, MailID, Class, UniqueID) 
	values 
    (1, 'Adda Wilmot', 'pTqfg65O', 'awilmot0@facebook.com', '12-C', 14569),
	(2, 'Ulrikaumeko MacIntyre', 'KZYteachersfR6rL7d', 'umacintyre1@mapy.cz', '12-B', 12494),
	(3, 'Rodolfo Queripel', 'Zh3I7kjQY1JN', 'rqueripel2@dagondesign.com', '12-F', 15555),
	(4, 'Alric Freiburger', 'L8Dg1bhMa', 'afreiburger3@slate.com', '12-A', 15590),
	(5, 'Isabel Doogan', 't2tmb4Pc', 'idoogan4@upenn.edu', '12-F', 16705),
	(6, 'Becky Beausang', 'FnnITYOxg', 'bbeausang5@netscape.com', '12-B', 13587),
	(7, 'Marys Everley', 'DL9dR6WUG', 'meverley6@youtu.be', '12-B', 16236),
	(8, 'Kalila Roberto', 'YnylrPClniJ', 'kroberto7@usa.gov', '12-A', 51214),
	(9, 'Koressa Silber', 'lGNFH8l', 'ksilber8@guardian.co.uk', '12-A', 69603),
	(10, 'Cirilo Gouldsmith', 'LsrkLjJb', 'cgouldsmith9@imageshack.us', '12-A', 48107),
	(11, 'Thacher Matyashev', 'wb929BaKx9Y', 'tmatyasheva@edublogs.org', '12-F', 47228),
	(12, 'Pall Barrand', 'TPVEsVC', 'pbarrandb@japanpost.jp', '12-D', 17399),
	(13, 'Gunar Isakson', '4gbExXnO', 'gisaksonc@delicious.com', '12-B', 73628),
	(14, 'Conway Bozworth', 'Ltc6Qw7LIIw', 'cbozworthd@dion.ne.jp', '12-D', 51018),
	(15, 'Cyndia Skells', 'cXEpogY', 'cskellse@squidoo.com', '12-A', 56091),
	(16, "Laverne O'Fallowne", 'o2tl2Vthq', 'lofallownef@gnu.org', '12-A', 14107),
	(17, 'Geri Stonner', 'j6Jztkg', 'gstonnerg@jiathis.com', '12-C', 15170),
	(18, 'Ferdinande Alasdair', 'XCMBdHsQCXV', 'falasdairh@canalblog.com', '12-F', 68925),
	(19, 'Brenda Aldersley', 'i8oSBF', 'baldersleyi@gnu.org', '12-F', 19374),
	(20, 'Leanora Moresby', 'Oh5uUa3fCj', 'lmoresbyj@usda.gov', '12-B', 25449);
