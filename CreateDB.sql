create table teams (
	TeamID		int,
   TeamName		varchar(32) unique not null,
   City			varchar(32) not null,
   primary key(TeamID)
);

create table players (
	PlayerID		int,
   FirstName	varchar(32) not null,
   LastName		varchar(32) not null,
   TeamID		int,
   Position		varchar(32),
   Touchdowns	int,
   TotalYards  int,
   Salary		int,
   primary key(PlayerID),
   foreign key(TeamID) references teams(TeamID) on delete set null,
   check(Position in ('QB', 'WR', 'RB')),
   check(Salary > 0),
   check(Touchdowns >= 0)
);

create table games (
	GameID			int,
   Date				date,
   Stadium			varchar(32) not null,
   Result			char,
   Attendance		int,
   TicketRevenue	int,
   primary key(GameID),
   check(Result in ('L', 'W', 'T')),
   check(Attendance >= 0),
   check(TicketRevenue >= 0)
);

create table play (
	PlayerID	int,
   GameID	int,
   primary key(PlayerID, GameID),
   foreign key(PlayerID) references players(PlayerID) on delete cascade,
   foreign key(GameID) references games(GameID) on delete cascade
);
