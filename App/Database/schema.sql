DROP TABLE IF EXISTS restriction;

CREATE TABLE restriction(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dayOfWeek INTEGER NOT NULL,
  regexExpression TEXT NOT NULL,
  initTime TEXT NOT NULL,
  endTime TEXT NOT NULL
);

INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (4,"0$","6:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (0,"1$","6:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (0,"2$","6:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (1,"3$","6:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (1,"4$","6:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (2,"5$","6:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (2,"6$","6:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (3,"7$","6:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (3,"8$","6:00","9:30");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (4,"9$","6:00","9:30");

INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (4,"0$","16:00","21:00");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (0,"1$","16:00","21:00");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (0,"2$","16:00","21:00");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (1,"3$","16:00","21:00");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (1,"4$","16:00","21:00");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (2,"5$","16:00","21:00");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (2,"6$","16:00","21:00");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (3,"7$","16:00","21:00");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (3,"8$","16:00","21:00");
INSERT INTO restriction (dayOfWeek,regexExpression,initTime,endTime) Values (4,"9$","16:00","21:00");
