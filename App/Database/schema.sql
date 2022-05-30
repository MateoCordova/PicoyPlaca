DROP TABLE IF EXISTS restriction;

CREATE TABLE restriction(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dayOfWeek INTEGER NOT NULL,
  regexExpression TEXT NOT NULL,
  initTime TEXT NOT NULL,
  endTime TEXT NOT NULL
);

INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (4,"0$","7:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (0,"1$","7:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (0,"2$","7:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (1,"3$","7:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (1,"4$","7:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (2,"5$","7:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (2,"6$","7:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (3,"7$","7:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (3,"8$","7:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (4,"9$","7:00","9:30");

INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (4,"0$","16:00","19:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (0,"1$","16:00","19:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (0,"2$","16:00","19:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (1,"3$","16:00","19:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (1,"4$","16:00","19:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (2,"5$","16:00","19:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (2,"6$","16:00","19:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (3,"7$","16:00","19:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (3,"8$","16:00","19:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (4,"9$","16:00","19:30");
