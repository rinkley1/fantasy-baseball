# fantasy-baseball

# Why are we here
I do a yearly fantasy baseball league on ESPN with a bud and some people he knows.
I really wish I could see managerial stats so I could run tests and maybe see if
there's any interesting trends. I use "interesting" veeeeery loosely.
Anyhoo, since ESPN doesn't show these trends, I made a prgoram to at least capture
one of them.

# The league
10 teams, 23 weeks.
Each week, each team plays against another team in a "matchup."
Each matchup is an accumulation of stats in 10 categories.
The results of each category give you a win, a loss, or a tie.
So the sum of wins, losses, and ties adds up to 10.

# The goal
This program writes to a csv each team's accumulated win percentage after each week.
This win percentage is based on the 10 categories.
The formula for calculating the percentage is: (wins / (ties/2)) / (wins+losses+ties)

## What do I mean by accumulated?
Let's say at the end of Week 1, you went 5-5-0 (5 wins, 5 losses, 0 ties).
Your win percentage would be .5.
Let's say your Week 2 result did not go well. You went 2-8-0.
Instead of writing Week 2's win percentage (.2), I want to write the updated win percentage.
Running it through the formula, the results would be 7-13-0. Or a .35 win percentage.

Basically, I wanted to create a line chart that shows
each team's win percentage week by week.
I don't know how to do a chart in Python, but I can in Excel.
So this writes the csv that I can then use in Excel to make a graph. Cool.

## But classes...
I'm gonna say this right off the bat (baseball pun): I don't fully understand classes yet.
I originally wrote this without classes, and honestly I believe it's better without them,
but the practice is worth it. I think.

# The data
Of course, ESPN's fantasy app and browser experience is trash.
A big chunk of this program is just for reading the data in all its wonkiness.

But I'll also say that the way I got the data and CSV file is super inefficient
and may not work the same next year when I try this again.

The columns in the CSV are the 22 weeks.
The rows alternate team and corresponding result. So there are 20 rows.

## How I sourced the data:
I went to each week's results page, highlighted the necessary results
(which meant also highlighting a bunch of unneccessary stuff), and then copying
them to Excel. The formatting was wonky as shiffuh. But at least consistent
week by week! That means I could write a single program that goes week by week
to write my data.

I could have done this all manually and it definitely would have taken less time,
but it's nice to say I did it and maybe next year it will be faster?
