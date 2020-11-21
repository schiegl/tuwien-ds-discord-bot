from intent import Intent, IntentName
from typing import Optional
import discord
import random

from handlers.handler import MessageHandler


class TellWiseQuote(MessageHandler):
    """
    Tell a wise quote if some one asks for it

    Taken from: https://github.com/mhinz/vim-startify
    """

    def __init__(self):
        super().__init__(channels=[], intent_names=[IntentName.ask_for_wise_quote])

        self.quotes = [
            {
                "text": [
                    "Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it."
                ],
                "author": "Brian Kernighan",
            },
            {"text": ["If you don't finish then you're just busy, not productive."]},
            {
                "text": [
                    "Adapting old programs to fit new machines usually means adapting new machines to behave like old ones."
                ],
                "author": "Alan Perlis",
            },
            {
                "text": ["Fools ignore complexity. Pragmatists suffer it. Some can avoid it. Geniuses remove it."],
                "author": "Alan Perlis",
            },
            {
                "text": ["It is easier to change the specification to fit the program than vice versa."],
                "author": "Alan Perlis",
            },
            {"text": ["Simplicity does not precede complexity, but follows it."], "author": "Alan Perlis"},
            {"text": ["Optimization hinders evolution."], "author": "Alan Perlis"},
            {
                "text": ["Recursion is the root of computation since it trades description for time."],
                "author": "Alan Perlis",
            },
            {
                "text": [
                    "It is better to have 100 functions operate on one data structure than 10 functions on 10 data structures."
                ],
                "author": "Alan Perlis",
            },
            {
                "text": [
                    "There is nothing quite so useless as doing with great efficiency something that should not be done at all."
                ],
                "author": "Peter Drucker",
            },
            {
                "text": ["If you don't fail at least 90% of the time, you're not aiming high enough."],
                "author": "Alan Kay",
            },
            {
                "text": [
                    "I think a lot of new programmers like to use advanced data structures and advanced language features as a way of demonstrating their ability. I call it the lion-tamer syndrome. Such demonstrations are impressive, but unless they actually translate into real wins for the project, avoid them."
                ],
                "author": "Glyn Williams",
            },
            {"text": ["I would rather die of passion than of boredom."], "author": "Vincent Van Gogh"},
            {
                "text": [
                    "If a system is to serve the creative spirit, it must be entirely comprehensible to a single individual."
                ],
            },
            {
                "text": [
                    "The computing scientist's main challenge is not to get confused by the complexities of his own making."
                ],
                "author": "Edsger W. Dijkstra",
            },
            {
                "text": [
                    "Progress in a fixed context is almost always a form of optimization. Creative acts generally don't stay in the context that they are in."
                ],
                "author": "Alan Kay",
            },
            {
                "text": [
                    "The essence of XML is this: the problem it solves is not hard, and it does not solve the problem well."
                ],
                "author": "Phil Wadler",
            },
            {
                "text": ["A good programmer is someone who always looks both ways before crossing a one-way street."],
                "author": "Doug Linder",
            },
            {"text": ['Patterns mean "I have run out of language."'], "author": "Rich Hickey"},
            {
                "text": [
                    "Always code as if the person who ends up maintaining your code is a violent psychopath who knows where you live."
                ],
                "author": "John Woods",
            },
            {
                "text": [
                    "Unix was not designed to stop its users from doing stupid things, as that would also stop them from doing clever things."
                ],
            },
            {
                "text": [
                    "Contrary to popular belief, Unix is user friendly. It just happens to be very selective about who it decides to make friends with."
                ],
            },
            {
                "text": [
                    "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."
                ],
            },
            {
                "text": [
                    "There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies, and the other way is to make it so complicated that there are no obvious deficiencies."
                ],
                "author": "C.A.R. Hoare",
            },
            {
                "text": ["If you don't make mistakes, you're not working on hard enough problems."],
                "author": "Frank Wilczek",
            },
            {
                "text": ["If you don't start with a spec, every piece of code you write is a patch."],
                "author": "Leslie Lamport",
            },
            {"text": ["Caches are bugs waiting to happen."], "author": "Rob Pike"},
            {
                "text": ["Abstraction is not about vagueness, it is about being precise at a new semantic level."],
                "author": "Edsger W. Dijkstra",
            },
            {
                "text": [
                    "dd is horrible on purpose. It's a joke about OS/360 JCL. But today it's an internationally standardized joke. I guess that says it all."
                ],
                "author": "Rob Pike",
            },
            {"text": ["All loops are infinite ones for faulty RAM modules."]},
            {
                "text": ["All idioms must be learned. Good idioms only need to be learned once."],
                "author": "Alan Cooper",
            },
            {
                "text": [
                    "For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled."
                ],
                "author": "Richard Feynman",
            },
            {
                "text": [
                    "If programmers were electricians, parallel programmers would be bomb disposal experts. Both cut wires."
                ],
                "author": "Bartosz Milewski",
            },
            {
                "text": [
                    "Computers are harder to maintain at high altitude. Thinner air means less cushion between disk heads and platters. Also more radiation."
                ],
            },
            {"text": ["Almost every programming language is overrated by its practitioners."], "author": "Larry Wall"},
            {"text": ["Fancy algorithms are slow when n is small, and n is usually small."], "author": "Rob Pike"},
            {"text": ["Methods are just functions with a special first argument."], "author": "Andrew Gerrand"},
            {
                "text": [
                    "Care about your craft.",
                    "Why spend your life developing software unless you care about doing it well?",
                ],
            },
            {
                "text": [
                    "Provide options, don't make lame excuses.",
                    "Instead of excuses, provide options. Don't say it can't be done; explain what can be done.",
                ],
            },
            {
                "text": [
                    "Be a catalyst for change.",
                    "You can't force change on people. Instead, show them how the future might be and help them participate in creating it.",
                ],
            },
            {
                "text": [
                    "Make quality a requirements issue.",
                    "Involve your users in determining the project's real quality requirements.",
                ],
            },
            {
                "text": [
                    "Critically analyze what you read and hear.",
                    "Don't be swayed by vendors, media hype, or dogma. Analyze information in terms of you and your project.",
                ],
            },
            {
                "text": [
                    "DRY - Don't Repeat Yourself.",
                    "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.",
                ],
            },
            {
                "text": [
                    "Eliminate effects between unrelated things.",
                    "Design components that are self-contained, independent, and have a single, well-defined purpose.",
                ],
            },
            {
                "text": [
                    "Use tracer bullets to find the target.",
                    "Tracer bullets let you home in on your target by trying things and seeing how close they land.",
                ],
            },
            {"text": ["Program close to the problem domain.", "Design and code in your user's language."],},
            {
                "text": [
                    "Iterate the schedule with the code.",
                    "Use experience you gain as you implement to refine the project time scales.",
                ],
            },
            {
                "text": [
                    "Use the power of command shells.",
                    "Use the shell when graphical user interfaces don't cut it.",
                ],
            },
            {
                "text": [
                    "Always use source code control.",
                    "Source code control is a time machine for your work - you can go back.",
                ],
            },
            {
                "text": [
                    "Don't panic when debugging",
                    "Take a deep breath and THINK! about what could be causing the bug.",
                ],
            },
            {
                "text": [
                    "Don't assume it - prove it.",
                    "Prove your assumptions in the actual environment - with real data and boundary conditions.",
                ],
            },
            {
                "text": [
                    "Write code that writes code.",
                    "Code generators increase your productivity and help avoid duplication.",
                ],
            },
            {
                "text": [
                    "Design With contracts.",
                    "Use contracts to document and verify that code does no more and no less than it claims to do.",
                ],
            },
            {
                "text": [
                    "Use assertions to prevent the impossible.",
                    "Assertions validate your assumptions. Use them to protect your code from an uncertain world.",
                ],
            },
            {
                "text": [
                    "Finish what you start.",
                    "Where possible, the routine or object that allocates a resource should be responsible for deallocating it.",
                ],
            },
            {
                "text": [
                    "Configure, don't integrate.",
                    "Implement technology choices for an application as configuration options, not through integration or engineering.",
                ],
            },
            {"text": ["Analyze workflow to improve concurrency.", "Exploit concurrency in your user's workflow."],},
            {
                "text": [
                    "Always design for concurrency.",
                    "Allow for concurrency, and you'll design cleaner interfaces with fewer assumptions.",
                ],
            },
            {
                "text": [
                    "Use blackboards to coordinate workflow.",
                    "Use blackboards to coordinate disparate facts and agents, while maintaining independence and isolation among participants.",
                ],
            },
            {
                "text": [
                    "Estimate the order of your algorithms.",
                    "Get a feel for how long things are likely to take before you write code.",
                ],
            },
            {
                "text": [
                    "Refactor early, refactor often.",
                    "Just as you might weed and rearrange a garden, rewrite, rework, and re-architect code when it needs it. Fix the root of the problem.",
                ],
            },
            {
                "text": [
                    "Test your software, or your users will.",
                    "Test ruthlessly. Don't make your users find bugs for you.",
                ],
            },
            {
                "text": [
                    "Don't gather requirements - dig for them.",
                    "Requirements rarely lie on the surface. They're buried deep beneath layers of assumptions, misconceptions, and politics.",
                ],
            },
            {
                "text": [
                    "Abstractions live longer than details.",
                    "Invest in the abstraction, not the implementation. Abstractions can survive the barrage of changes from different implementations and new technologies.",
                ],
            },
            {
                "text": [
                    "Don't think outside the box - find the box.",
                    'When faced with an impossible problem, identify the real constraints. Ask yourself: "Does it have to be done this way? Does it have to be done at all?"',
                ],
            },
            {
                "text": [
                    "Some things are better done than described.",
                    "Don't fall into the specification spiral - at some point you need to start coding.",
                ],
            },
            {
                "text": [
                    "Costly tools don't produce better designs.",
                    "Beware of vendor hype, industry dogma, and the aura of the price tag. Judge tools on their merits.",
                ],
            },
            {
                "text": [
                    "Don't use manual procedures.",
                    "A shell script or batch file will execute the same instructions, in the same order, time after time.",
                ],
            },
            {"text": ["Coding ain't done 'til all the Tests run.", "'Nuff said."]},
            {
                "text": [
                    "Test state coverage, not code coverage.",
                    "Identify and test significant program states. Just testing lines of code isn't enough.",
                ],
            },
            {
                "text": [
                    "English is just a programming language.",
                    "Write documents as you would write code: honor the DRY principle, use metadata, MVC, automatic generation, and so on.",
                ],
            },
            {
                "text": [
                    "Gently exceed your users' expectations.",
                    "Come to understand your users' expectations, then deliver just that little bit more.",
                ],
            },
            {
                "text": [
                    "Think about your work.",
                    "Turn off the autopilot and take control. Constantly critique and appraise your work.",
                ],
            },
            {
                "text": [
                    "Don't live with broken windows.",
                    "Fix bad designs, wrong decisions, and poor code when you see them.",
                ],
            },
            {
                "text": [
                    "Remember the big picture.",
                    "Don't get so engrossed in the details that you forget to check what's happening around you.",
                ],
            },
            {"text": ["Invest regularly in your knowledge portfolio.", "Make learning a habit."]},
            {
                "text": [
                    "It's both what you say and the way you say it.",
                    "There's no point in having great ideas if you don't communicate them effectively.",
                ],
            },
            {
                "text": [
                    "Make it easy to reuse.",
                    "If it's easy to reuse, people will. Create an environment that supports reuse.",
                ],
            },
            {
                "text": [
                    "There are no final decisions.",
                    "No decision is cast in stone. Instead, consider each as being written in the sand at the beach, and plan for change.",
                ],
            },
            {
                "text": [
                    "Prototype to learn.",
                    "Prototyping is a learning experience. Its value lies not in the code you produce, but in the lessons you learn.",
                ],
            },
            {
                "text": [
                    "Estimate to avoid surprises.",
                    "Estimate before you start. You'll spot potential problems up front.",
                ],
            },
            {
                "text": [
                    "Keep knowledge in plain text.",
                    "Plain text won't become obsolete. It helps leverage your work and simplifies debugging and testing.",
                ],
            },
            {
                "text": [
                    "Use a single editor well.",
                    "The editor should be an extension of your hand; make sure your editor is configurable, extensible, and programmable.",
                ],
            },
            {
                "text": [
                    "Fix the problem, not the blame.",
                    "It doesn't really matter whether the bug is your fault or someone else's - it is still your problem, and it still needs to be fixed.",
                ],
            },
            {
                "text": [
                    '"select" isn\'t broken.',
                    "It is rare to find a bug in the OS or the compiler, or even a third-party product or library. The bug is most likely in the application.",
                ],
            },
            {
                "text": [
                    "Learn a text manipulation language.",
                    "You spend a large part of each day working with text. Why not have the computer do some of it for you?",
                ],
            },
            {
                "text": [
                    "You can't write perfect software.",
                    "Software can't be perfect. Protect your code and users from the inevitable errors.",
                ],
            },
            {"text": ["Crash early.", "A dead program normally does a lot less damage than a crippled one."],},
            {
                "text": [
                    "Use exceptions for exceptional problems.",
                    "Exceptions can suffer from all the readability and maintainability problems of classic spaghetti code. Reserve exceptions for exceptional things.",
                ],
            },
            {
                "text": [
                    "Minimize coupling between modules.",
                    'Avoid coupling by writing "shy" code and applying the Law of Demeter.',
                ],
            },
            {
                "text": [
                    "Put abstractions in code, details in metadata.",
                    "Program for the general case, and put the specifics outside the compiled code base.",
                ],
            },
            {
                "text": [
                    "Design using services.",
                    "Design in terms of services-independent, concurrent objects behind well-defined, consistent interfaces.",
                ],
            },
            {
                "text": [
                    "Separate views from models.",
                    "Gain flexibility at low cost by designing your application in terms of models and views.",
                ],
            },
            {
                "text": [
                    "Don't program by coincidence.",
                    "Rely only on reliable things. Beware of accidental complexity, and don't confuse a happy coincidence with a purposeful plan.",
                ],
            },
            {
                "text": [
                    "Test your estimates.",
                    "Mathematical analysis of algorithms doesn't tell you everything. Try timing your code in its target environment.",
                ],
            },
            {"text": ["Design to test.", "Start thinking about testing before you write a line of code."],},
            {
                "text": [
                    "Don't use wizard code you don't understand.",
                    "Wizards can generate reams of code. Make sure you understand all of it before you incorporate it into your project.",
                ],
            },
            {
                "text": [
                    "Work with a user to think like a user.",
                    "It's the best way to gain insight into how the system will really be used.",
                ],
            },
            {
                "text": [
                    "Use a project glossary.",
                    "Create and maintain a single source of all the specific terms and vocabulary for a project.",
                ],
            },
            {
                "text": [
                    "Start when you're ready.",
                    "You've been building experience all your life. Don't ignore niggling doubts.",
                ],
            },
            {
                "text": [
                    "Don't be a slave to formal methods.",
                    "Don't blindly adopt any technique without putting it into the context of your development practices and capabilities.",
                ],
            },
            {
                "text": [
                    "Organize teams around functionality.",
                    "Don't separate designers from coders, testers from data modelers. Build teams the way you build code.",
                ],
            },
            {
                "text": [
                    "Test early. Test often. Test automatically.",
                    "Tests that run with every build are much more effective than test plans that sit on a shelf.",
                ],
            },
            {
                "text": [
                    "Use saboteurs to test your testing.",
                    "Introduce bugs on purpose in a separate copy of the source to verify that testing will catch them.",
                ],
            },
            {
                "text": [
                    "Find bugs once.",
                    "Once a human tester finds a bug, it should be the last time a human tester finds that bug. Automatic tests should check for it from then on.",
                ],
            },
            {
                "text": [
                    "Sign your work.",
                    "Craftsmen of an earlier age were proud to sign their work. You should be, too.",
                ],
            },
            {"text": ["Think twice, code once."]},
            {"text": ["No matter how far down the wrong road you have gone, turn back now."]},
            {"text": ["Why do we never have time to do it right, but always have time to do it over?"]},
            {"text": ["Weeks of programming can save you hours of planning."]},
            {"text": ["To iterate is human, to recurse divine."], "author": "L. Peter Deutsch"},
            {"text": ["Computers are useless. They can only give you answers."], "author": "Pablo Picasso"},
            {
                "text": [
                    "The question of whether computers can think is like the question of whether submarines can swim."
                ],
                "author": "Edsger W. Dijkstra",
            },
            {
                "text": [
                    "It's ridiculous to live 100 years and only be able to remember 30 million bytes. You know, less than a compact disc. The human condition is really becoming more obsolete every minute."
                ],
                "author": "Marvin Minsky",
            },
            {
                "text": [
                    "The city's central computer told you? R2D2, you know better than to trust a strange computer!"
                ],
                "author": "C3PO",
            },
            {
                "text": [
                    "Most software today is very much like an Egyptian pyramid with millions of bricks piled on top of each other, with no structural integrity, but just done by brute force and thousands of slaves."
                ],
                "author": "Alan Kay",
            },
            {
                "text": [
                    'I\'ve finally learned what "upward compatible" means. It means we get to keep all our old mistakes.'
                ],
                "author": "Dennie van Tassel",
            },
            {
                "text": [
                    "There are two major products that come out of Berkeley: LSD and UNIX. We don't believe this to be a coincidence."
                ],
                "author": "Jeremy S. Anderson",
            },
            {
                "text": [
                    "The bulk of all patents are crap. Spending time reading them is stupid. It's up to the patent owner to do so, and to enforce them."
                ],
                "author": "Linus Torvalds",
            },
            {"text": ["Controlling complexity is the essence of computer programming."], "author": "Brian Kernighan"},
            {
                "text": [
                    "Complexity kills. It sucks the life out of developers, it makes products difficult to plan, build and test, it introduces security challenges, and it causes end-user and administrator frustration."
                ],
                "author": "Ray Ozzie",
            },
            {
                "text": ["The function of good software is to make the complex appear to be simple."],
                "author": "Grady Booch",
            },
            {
                "text": [
                    "There's an old story about the person who wished his computer were as easy to use as his telephone. That wish has come true, since I no longer know how to use my telephone."
                ],
                "author": "Bjarne Stroustrup",
            },
            {
                "text": ['There are only two industries that refer to their customers as "users".'],
                "author": "Edward Tufte",
            },
            {
                "text": [
                    "Most of you are familiar with the virtues of a programmer. There are three, of course: laziness, impatience, and hubris."
                ],
                "author": "Larry Wall",
            },
            {
                "text": [
                    "Computer science education cannot make anybody an expert programmer any more than studying brushes and pigment can make somebody an expert painter."
                ],
                "author": "Eric S. Raymond",
            },
            {
                "text": ["Optimism is an occupational hazard of programming; feedback is the treatment."],
                "author": "Kent Beck",
            },
            {"text": ["First, solve the problem. Then, write the code."], "author": "John Johnson"},
            {
                "text": [
                    "Measuring programming progress by lines of code is like measuring aircraft building progress by weight."
                ],
                "author": "Bill Gates",
            },
            {
                "text": ["Don't worry if it doesn't work right. If everything did, you'd be out of a job."],
                "author": "Mosher's Law of Software Engineering",
            },
            {
                "text": ["A LISP programmer knows the value of everything, but the cost of nothing."],
                "author": "Alan J. Perlis",
            },
            {
                "text": ["All problems in computer science can be solved with another level of indirection."],
                "author": "David Wheeler",
            },
            {
                "text": [
                    "Functions delay binding; data structures induce binding. Moral: Structure data late in the programming process."
                ],
                "author": "Alan J. Perlis",
            },
            {"text": ["Easy things should be easy and hard things should be possible."], "author": "Larry Wall"},
            {"text": ["Nothing is more permanent than a temporary solution."]},
            {
                "text": ["If you can't explain something to a six-year-old, you really don't understand it yourself."],
                "author": "Albert Einstein",
            },
            {"text": ["All programming is an exercise in caching."], "author": "Terje Mathisen"},
            {"text": ["Software is hard."], "author": "Donald Knuth"},
            {"text": ["They did not know it was impossible, so they did it!"], "author": "Mark Twain"},
            {
                "text": [
                    "The object-oriented model makes it easy to build up programs by accretion. What this often means, in practice, is that it provides a structured way to write spaghetti code."
                ],
                "author": "Paul Graham",
            },
            {
                "text": [
                    "Question: How does a large software project get to be one year late?",
                    "Answer: One day at a time!",
                ],
            },
            {
                "text": [
                    "The first 90% of the code accounts for the first 90% of the development time. The remaining 10% of the code accounts for the other 90% of the development time."
                ],
                "author": "Tom Cargill",
            },
            {
                "text": [
                    "In software, we rarely have meaningful requirements. Even if we do, the only measure of success that matters is whether our solution solves the customer's shifting idea of what their problem is."
                ],
                "author": "Jeff Atwood",
            },
            {
                "text": [
                    "If debugging is the process of removing bugs, then programming must be the process of putting them in."
                ],
                "author": "Edsger W. Dijkstra",
            },
            {"text": ["640K ought to be enough for anybody."], "author": "Bill Gates, 1981"},
            {"text": ["To understand recursion, one must first understand recursion."], "author": "Stephen Hawking"},
            {
                "text": [
                    "Developing tolerance for imperfection is the key factor in turning chronic starters into consistent finishers."
                ],
                "author": "Jon Acuff",
            },
            {
                "text": [
                    "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it."
                ],
                "author": "Patrick McKenzie",
            },
            {
                "text": [
                    "The average user doesn't give a damn what happens, as long as (1) it works and (2) it's fast."
                ],
                "author": "Daniel J. Bernstein",
            },
            {
                "text": ["Walking on water and developing software from a specification are easy if both are frozen."],
                "author": "Edward V. Berard",
            },
            {
                "text": [
                    "Be curious. Read widely. Try new things. I think a lot of what people call intelligence boils down to curiosity."
                ],
                "author": "Aaron Swartz",
            },
            {
                "text": ["What one programmer can do in one month, two programmers can do in two months."],
                "author": "Frederick P. Brooks",
            },
        ]

        self.unknown_authors = [
            "He who shall not be named",
            "A friend of a friend",
            "Confidential",
            "Me 😅",
        ]

    def handle(self, message: discord.Message, intent: Intent) -> Optional[str]:
        if intent.probability > 0.9:
            quote = random.choice(self.quotes)
            author = quote.get("author", random.choice(self.unknown_authors))
            return "> " + "\n> ".join(quote["text"]) + f"\n>  *- {author}*"
        else:
            return None

