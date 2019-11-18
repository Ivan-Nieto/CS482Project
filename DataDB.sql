set sql_safe_updates = 0;

delete from play;
delete from games;
delete from players;
delete from teams;

insert into teams values (1001, 'Donkeys', 'Denver');
insert into teams values (2002, 'Indians', 'Washington D.C.');
insert into teams values (3003, 'Team Brady', 'Boston');
insert into teams values (4004, 'Not 2017 Champs', 'Atlanta');
insert into teams values (5005, 'Leaving to Vegas', 'Oakland');

insert into players values(101, 'Thomas', 'Brady', 3003, 'QB', 5, 272, 500000);
insert into players values(202, 'Odell', 'Beckham', 1001, 'WR', 7, 423, 100000);
insert into players values(303, 'Ivan', 'Nieto', 2002, 'RB', 4, 132, 200000);
insert into players values(404, 'Mason', 'Salcido', 5005, 'WR', 1, 548, 350000);
insert into players values(505, 'Matt', 'Ryan', 4004, 'QB', 0, 573, 240000);

insert into games values(11,'2018-12-3', 'Some Stadium', 'L', 55000, 780000);
insert into games values(22,'2019-5-17', 'Other Stadium', 'W', 70000, 630000);
insert into games values(33,'2019-1-13', 'Different Stadium', 'W', 29000, 380000);
insert into games values(44,'2019-2-14', 'An Arena', 'L', 74000, 760000);
insert into games values(55,'2019-4-20', 'The Stadium', 'T', 81000, 930000);

insert into play values(505, 44);
insert into play values(303, 22);
insert into play values(101, 33);
insert into play values(202, 11);
insert into play values(404, 55);
