person(john,date(1990,5,15)).
person(mary,date(1985,9,23)).
person(david,date(1995,2,8)).
person(lisa,date(2000,11,30)).
find_person(Name, DOB) :-
    person(Name,DOB).
born_in_year(Year, Name) :-
    person(Name,date(Year,_,_)).
born_in_month(Month,Name) :-
    person(Name,date(_,Month,_)).
born_on_day(Day,Month, Name) :-
    person(Name, date(_,Month, Day)).
