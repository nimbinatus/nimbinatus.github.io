---
title: Adding Logs to Legacy Applications
author: Laura Santamaria
category: logs
slug: adding-logs-to-legacy
date: 15 November 2019
tags: logging, legacy-apps
status: published
---

As the final interactive in my mini-workshop at DeveloperWeek Austin 2019, I posed the following scenario to the audience:
    
> You have a legacy application that has not been updated in 5 years. The system is running Python 2, which is sunsetting in January 2020. The system recently had its first incident in nearly 4 years, and your team was among the group that had to bring it back up. The logs that you received were not very helpful, and bringing the production instance back up ended up being a lot of trial and error.
>
> Management has decided all applications must be on Python 3 by the end of code freeze in January 2020. Your team has been tasked with updating the application to use Python 3. It's the ideal time to add proper logging. How would you go about planning and executing that logging update?

The scenario generated a lot of discussion, and people had some very good answers. However, someone on Twitter (thanks for the question, @russellyazbeck!) pointed out to me that I completely forgot to provide my take on the same scenario. Whoops! I did respond in a thread on Twitter, but I'd like to lay it out and expand on it a bit here as it's definitely easier to find.

First and foremost, the members of the audience that started with bringing everyone together were spot on. You can certainly have your own data that your immediate team gathered during the incident, reaching out to the rest of the teams that responded to the incident and gathering their data is also important. Why? They have different perspectives. It's very easy to get lost in your own context and stop noticing quirks or issues unique to your programming language of choice, to a platform you're somewhat familiar with, or even to a team that you have worked with in the past. Ask anyone who has ever taught a concept to someone else successfully, and you'll find that nine times out of ten, those people will mention how they were surprised initially where someone got lost or how hard it was to avoid jargon that needed further explanation. So ensure you get data from anyone who was involved in that incident so you can start understanding what other people might need to understand the same issue. 

Once you've gotten everyone together, start talking about the ideal incident response and the ideal data that you would have gathered. What should those logs have shown? What data did you actually need? In addition, what data was just noise? Was there any data that duplicated information? In addition, you can use this time to discuss which log levels would be useful for each type of data. Log levels help reduce or structure the noise coming from a logging system. Since a good production system allows for tuning the logs based on which environment you're in (dev, test/QA, staging, prod, or some combination thereof) and since any and all teams doing ops work on said system would likely love you if they don't have to decide whether a log raised by your system is a deprecation warning (WARN) or something that isn't acting right but won't take down the whole house of cards (ERROR) or something that took down everything including your databases and networking (CRITICAL), coming to a consensus on which logging levels are necessary and how to define them is really important both now and in the future.

Now that you have a much better idea of what kind of data you actually needed, you would pick a library or logging structure that could help give you what you needed. If you were in a scenario that had a bunch of other apps going, as would be likely in a scenario like this where there's a legacy application and multiple teams that likely are working on multiple projects, I'd definitely look to a structured logs library like [structlog](http://www.structlog.org/en/stable/). While I could roll my own on top of the standard logging library, my guess is the rest of the team (and future team members) would likely find a library with good docs and standardized uses much easier to use to maintain good logs in the long run. An opinionated logging library would likely be best to ensure everyone logs well.  Personally, I wouldn't use only text logs for this sort of situation, even if there's only one application that your company owns. Start as you intend to continue so that it's a lot easier down the line to ensure future systems are easier for others to onboard onto with similar features, common style, and other familiar elements. However, you have to keep in mind that this mentality includes a point that I made in the workshop: The audience of structured logs isn't really a human or a set of humans, but rather many machines parsing the data for you.

By the way, I want to point something out. I chose the Python 2 to Python 3 conversion scenario because it's one of those moments that's an ideal time to add logs. You're already in the codebase digging around and touching everything. You're getting to know what's there, so you're unlikely to skip anything major (well, assuming you're not using [six](https://pypi.org/project/six/) or the built-in [2to3](https://docs.python.org/3/library/2to3.html)). It's also the ideal time, as noted by a few folks in the audience, to add in a deprecation warning for anything that relied on the Python 2 conventions for hitting the application. However, it is a bit of a red herring. You can add these kinds of logs to any system at any time. Legacy systems are often viewed as the most dreaded to work with, hence the scenario, and incidents are one of the ideal times to take a step back and understand what data is flowing through your system. However, you can use this same thought process for a modern application, an application that hasn't had an incident, or even an application that's brand new. Walk through the scenario as if your application just had that moment happen (or knock it over deliberately in dev or staging when those environments are not in use for anything critical), and see what comes out of the brainstorming exercise with the various teams that would theoretically be involved. Then add logs and monitor the outcome.

How else would you respond to this scenario I laid out here? Come find me on [Twitter](https://www.twitter.com/nimbinatus) and let me know.

## IRL

I'm going to be at KubeCon North America 2019 this coming week! Come hack on the broken k8s repo with me (more from that [here]({filename}2019-10-22-introducing-broken-k8s.md)), and see what swag I have for folks that contribute environments or significantly update documentation. I'll be at the LogDNA booth or floating around the conference.