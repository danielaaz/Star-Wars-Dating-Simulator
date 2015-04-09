# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
#blue is some dude's favorite color
image han solo = "hansolo.png"
image black picture = "black.jpg"
image sun down = "sunset.jpeg"
image leia organa = "princessleia.png"
# Declare characters used by this game.
define h = Character('Han Solo', color="#c8ffc8")
define p = Character("[name]")
define y = Character("Mr. Youngblood", color="#8FFF85")
define l = Character("Leia", color="#B500C9")
define r = Character("R2-D2", color="#B500C9")
# The game starts here.
label start:
    $ hanpoints = 0
    $ intellect = 0
    $ books = 0
    $ math = 0
    $ music = 0
    $ day = 0
    $ leiaElective = False
    $ leiapoints = 0
    $ isFriday = False
    $ hanlove = False
    $ hasStuff = False
    $ hanEnding = False
    $ r2points = 0
    $ handidit = False
    $ r2didit = False
    $ r2meeting = False
    $ hanmeeting = True
    #crappily mysterious music
    show black picture
    "Welcome to Coruscant High! We aren't the largest school around, but our students certainly make up for that."
    "Anyways, excuse me, but are you a boy or a girl? You didn't really tell us."
    menu:
        "Female":
            "Oh, I see."
        "Male":
            "Huh, really? Surprising, I guess."
    python:
        name = renpy.input("So, before I forget, what is your name?")
        name = name.strip()
        if not name:
                name = "Elizabeth"
    "Great, we look forward to seeing you, [name]! What a weird name, though."
    "You should keep in mind that, if you want to pursue relationships and increase your capabilities, you should choose the right activities."
    p "(...)"
    p "(Man, what is going on? I can't move or see anything. How typical.)"
    hide black screen
    jump firstday
label firstday:
    #birds chirp, sunlight, something ok i guess, bedroom perhaps
    $ day += 1
    "GET TRANSITIONS"
    p "(Yaaaaaawwwn...ugh, why is the sun so bright? Can't it just move away from the window?)"
    p "(Man, what a weird dream. I already registered with the school a while before today...)"
    p "(I kept one eye shut until I could withstand the sun hitting both of them and rolled over. I knew that today would be important, but I stayed up late enjoying my last day of summer.)"
    p "(Oh, well. I’d better get ready, and quickly; I’ll have to walk, and it won’t exactly take seconds to get there.)"
    #boom! transition! school! omg!
    "filler/reminder to PUT A TRANSITION HERE"
    p "(I look up at the gleaming gates of Coruscant High, wondering whether they plan on keeping me in or out. The sakura trees are in bloom, even though it’s summer, but I don’t think anyone has noticed.)"
    p "(There are a few students waiting outside with me. I see a faintly familiar face, but I’m too nervous to strike up a conversation. It’s the first day of school at this place, and the only people I know are ones I talked to, at most, for 5 minutes before being swept through the hallways.)"
    "jabba the hut convo as soon as picture is editing and inserted"
    "bell sound reminder"
    p "(Anyways, a bell rings from somewhere. I don’t really know how or where, but right then the gates open and we all pour in excitedly.)"
    "more transition"
    p "(As I’m in the second half of the students looking for a seat near their friends, most are taken. Since I don’t know anyone, it doesn’t matter too much to me where I sit. I slide into a seat near the window and next to a guy who seems tired but happy. He looks my way, then leans over and gets ready to speak.)"
    show han solo at left:
        zoom 1.5
    h "Hey, beautiful - even if you aren’t as beautiful as me. What’s your name?"
    $ hanmeeting = True
    p "I'm [name]. You?"
    h "Han Solo. You’re new, aren’t you? It’s either that, or I’m less observant than I realized."
    p "Yup! My family came from France. For no reason, really, other than that we wanted to see Japan."
    h "Sounds like you'll have some fun. I'll have to show you around sometime."
    p "(He turns in his chair and slumps over slightly as we wait for our teacher to show up.)"
    p "(...)"
    p "(Gosh, we've been waiting for 10 minutes now and there's no sign of our teacher. Where could he be?)"
    y "Hey, class. Welcome to Curscant High - who are all of you, anyways?"
    p "(Han Solo is trying to whisper something to me...)"
    h "Heh, Mr. Youngblood's been here for ages, but he's pretty forgetful. Never remembers any of us."
    p "Aww, poor guy. It must be hard for him."
    h "Ah, you won't feel so bad for him. Other than being forgetful, he's a pretty great teacher, though rumor has it that he's literally set students on fire before."
    y "HEY! YOU TWO! Stop talking over me on day one! You haven't even had time to determine whether or not I'm one of your asshole teachers yet!"
    hide han solo
    p "(The class quieted down then. Han Solo looked only slightly startled, though. Either he's used to this crazy old man's teaching or he just doesn't care about much.)"
    y "Ahem! Now that you slackers have quieted down, we'll start our first lesson. Other teachers may try to explain how this school works, but I'm not that teacher."
    "transition!!?!?"
    p "(Well, it's lunch time now.)"
    p "(Great...I don't know anyone here in this sea of unfamiliar faces. I could try to find Han Solo, or just find any place. What should I do?)"
    menu:
        "Find Han Solo":
            jump hansololunch
        "Sit somewhere else":
            jump normallunch
    jump hansololove
label hansololove:
    show sun down:
        zoom .5
    p "(Urk. I've been waiting for about 20 minutes now, and my heart's been pounding nonstop. Without thinking, I began to mutter aloud.)"
    p "I really hope that he'll show up..."
    p "(Wait, what am I even doing? I should just wait in silence.)"
    show han solo at left:
        zoom 1.5
    h "What, did you think I'd stand you up?"
    p "Well, no, but..."
    h "Then quit it. I'm here now."
    p "You're right. So tell me, why are we here at the side of the road?"
    h "Aside from the occasional car passing by, just look down the railing and tell me that isn't a beautiful sight."
    p "(I've always been a little nervous about heights, but I look down, and it's rather stunning.)"
    p "(There's a small river carving its way through the trees and small houses dotted around the hillside, but the sky is what ties it all together.)"
    p "Wow. It's breathtaking. How did you end up finding this view?"
    h "One day, my mother went off of the edge around here while driving, before the railing was installed."
    h "She somehow survived and landed in the river; I was shown this place at some point. I think it looks a lot nicer without a miserable cross stuck in the ground."
    h "Anyways, I've taken a few gals up here every now and then. My heart belongs to you, though."
    p "I see. Actually, I have something for you..."
    if hasStuff == True:
        menu:
            "Teddy Bear":
                h "For me? Thanks."
            "Chocolate":
                h "Looks delicious. My stomach will treasure it."
            "Diamond":
                h "Woah there. I'm impressed that you found this for me."
    else:
        menu:
            "Teddy Bear":
                h "For me? Thanks."
            "Chocolate":
                h "Looks delicious. My stomach will treasure it."
    h "Come to think of it, I got you a little something myself."
    p "(He pulled something small out of his pocket. Han opened it, and a sparkling ring was revealed.)"
    p "(Han gently pulled my right hand towards him and slipped the ring onto my ring finger.)"
    p "Thanks, Han. The way it sparkles...it'll remind me of you."
    h "Anytime, [name]."
    p "(Although we were standing, he slid his arm around me.)"
    hide han solo
    show black picture1
    "You have received the Han Solo ending."
    "Thanks for making it this far. I don't know how you did it. Really. It's not like I had to write it all or anything."
    "Well, too bad you have to get all good endings to unlock the 'true' one!"
    "What a pain, amirite?"
    $ hanEnding = True
    return
label hansololunch:
    show han solo at left:
        zoom 1.5
    p "(I decided that I would find Han Solo and eat with him.)"
    p "(I waited in the long line for my food, scanned the cafeteria for him, and found a spot across from him.)"
    h "Hey."
    $ hanpoints += 1
    hide han solo
    jump afternoon
label normallunch:
    p "(I wasn't in the mood to sit with anyone else, so after getting my food I sat down alone and looked out the window while I was eating.)"
    jump afternoon
label afternoon:
    "transition"
    if hanpoints > 10 and hanlove == False:
        jump han_afternoon
    if day == 30:
        jump bad_end
    p "(Lunch is over, so now I can choose an elective class to go to. )"
    p "(Hmmm, which class?)"
    menu:
        "Math":
            jump math_class
        "Music":
            jump music_class
        "Literature":
            jump books_lol
label books_lol:
    p "(I decided to attend literature class.)"
    if leiaElective == True:
        l "Hello. I'm looking forward to today's class - I heard that we'll read some classics today!"
        $ leiapoints += 1
        $ books += 1
        jump end_day
    if books < 5:
        p "(Today, the teacher let us select poetry to read. Most of it is boring slush, but he seems to think otherwise.)"
        $ books += 1
        jump end_day
    p "(We dove right into the analysis of classic books we were not-so-subtly advised to read before class.)"
    $ books += 1
    jump end_day
label math_class:
    p "(I decided to attend math class.)"
    if r2meeting == True:
        r "Beep!"
        $ r2points += 1
    if math < 5:
            p "(Urgh...I didn't really understand what I was doing, but I think it helped me.)"
            $ math += 1
            jump end_day
    p "(We all worked on some large problems together. Thank the gods for calculators.)"
    $ math += 1
    jump end_day

label music_class:
    p "(I decided to attend music class.)"
    if music < 5:
        p "(Some people were able to hammer away on their own instruments.)"
        p "(That did not include me. I worked in a small group with the teacher, learning how to read music.)"
        $ music += 1
        jump end_day
    p "(I worked on a relatively simple guitar piece today. Maybe soon I can move on to a better one.)"
    $ music += 1
    jump end_day
label end_day:
    if day == 1:
        jump meet_leia
    if hanpoints > 5 and r2points > 5 and day > 15:
        jump r2_death
    "transition n stuff"
    "(It's evening now. What should I do?)"
    menu:
        "Be lazy":
            p "(Eh. I wasn't really feeling it tonight.)"
        "Don't be lazy":
            p "(What a tough choice.)"
            $ intellect += 1
    p "(Well, time to sleep now.)"
    jump morning
label meet_leia:
    p "(Finally, my first day has come to an end. It was fun, but it wore me out.)"
    p "(Before I leave, I'm stopped by a new face.)"
    show leia organa at right:
        zoom 0.7
    l "Hello there. I don't believe I've had the honor of seeing you before - what is your name?"
    p "[name]. What might yours be?"
    l "You can call me Leia."
    p "Will do."
    p "(This is as good a chance as any to ask her a question. What should I ask?)"
    menu:
        "What elective do you take?":
            l "I enjoy partaking in Literature."
            $ leiaElective = True
        "What class are you in?":
            l "I'm in class 2-C."
label morning:
    "chirp noise n whatever man"
    $ day += 1
    if day % 5 == 0:
        $ isFriday = True
    $ isFriday = False
    "It's day [day] of school today. I'd better get out of bed and get to school."
    jump schoolmorning
label schoolmorning:
    if isFriday == True:
        p "Thank gods it's Friday today."
    p "As usual, Mr. Youngblood was late. Somehow, he never fails to be late to class, only to deny it upon walking into class."
    p "(Sit next to...)"
    menu:
        "Han Solo":
            p "(I took a seat next to Han Solo. He glanced at me slightly before going into his aimless school day slouch.)"
            $ hanpoints += 1
        "Leia":
            p "(I took a seat next to Leia. She was preparing to take notes, as always.)"
            $ leiapoints += 1
        "R2-D2":
            p "(I took a seat next to R2. He was doing something enigmatic to me.)"
            $ r2points += 1
    p "(Mr. Youngblood's lecture was energetic with a dash of madness. He worries me sometimes.)"
    "transition"
    jump lunch
label han_afternoon:
    p "(Lunch just ended, so I walked straight to my locker on the third floor to grab my backpack and find an elective to do.)"
    h "Hey."
    p "(Han just came out of nowhere as I was rummaging through my locker - I was mildly startled, but more happy than alarmed.)"
    p "Hi! Next time, I wouldn't mind you being a bit less sneaky. (wow that sounds cheesy af but here's a note to fix it)"
    h "Well, sorry princess, but that's not going to happen anytime soon."
    p "Fine, then. I shouldn't have expected as much from the likes of you. What are you here for, anyway?"
    h "Oh, you know. The usual. Missing out on elective. However, this time, I'd like you to come with me - Chewy's not here today, so I need someone else."
    p "(Hmmm...missing elective won't make my parents or teachers happy. But if it's for Han Solo...)"
    p "(I threw my backpack back into my locker and shut it loudly.)"
    p "So, where are you taking me, in that case?"
    h "We can get pizza like Chewy and I do, or you can find a more romantic thing to do, if you please."
    p "Let's do something that's special to you."
    h "So, we'll do you?"
    p "(I totally set myself up for that. Typical high schooler stuff, I guess. What was I expecting?)"
    p "Lack of class aside, that is somewhat sweet of you to say. What about one of the local cafes?"
    h "I'm down with it. Which one, though? There are the hip and trendy joints, and then the European-style, mellow ones that suck you in with dim lighting for hours."
    p "A European one, definitely, unless you love eating 'new' and 'revolutionary' food while listening to loud hippie music."
    h "Ouch, what do you have against those cafes? Not that I like them, but it is a little harsh."
    p "Back in France, it was normal to frown at those. Then again, it was normal to frown at a lot of things, like Americans and English."
    h "Huh. Just part of your snobby culture, then? No matter. Let's go."
    p "(Instead of going to an elective, we hid in the bathrooms until electives started and headed out.)"
    h "If you see a teacher, just act like you're we're on our way to a class. I doubt we'll see anyone or get stopped, but on the off chance that we do, you'll know what to do."
    p "Uh...ok then. I'll try."
    p "(After Han said that, I think I walked a little bit more stiffly than I should have, and he noticed.)"
    h "Hey, lighten up, would you? Walking like that is going to make you look even more suspicious."
    p "Alright, but it was because of you telling me how I should act."
    p "(We made it out a side door with no problem. It felt pretty nice outside, too. Sunny, with a slight breeze blowing my hair around.)"
    h "See, that wasn't so hard. Mr. Youngblood would have been pretty disappointed in you if we were caught."
    p "Oh, I'm sure. But, with you, I didn't feel that we would run into any problems."
    h "Well, you were right. Not that I'm surprised, either. So, we're heading to La Craperie?"
    p "Yup! We'll find something there. I can help you identify food if you don't know what it is."
    h "Heh. Your culture really is as snobby as it can get."
    p "Riiight. Coming from you, I'm not accepting that."
    h "I can't say I'm not surprised."
    "transititon to cofe shope pls thank"
    p "Wow, these pastries look pretty good! What are you getting, Han?"
    h "You tell me."
    p "I think you'll do just fine with a simple almond croissant."
    h "Sounds delicious."
    p "Great. "
    $ hanlove = True
    jump end_day
label bad_end:
    show black picture
    p "(For some reason after lunch today, I felt sick. My head was throbbing, and my legs ached.)"
    p "(And yet, instead of going to the restroom or the school secretary, those aching legs took me out the front doors. I was going to miss class, but it didn't really matter at that moment.)"
    p "(I stumbled out onto the busy road in front of Coruscant High. There was a pretty red car that looked brand new zooming by.)"
    p "(I don't think the driver saw me. There was a sharp pain, and the feeling that I wasn't on the ground. After that, I lost all of my senses. My headache was finally gone forever.)"
    "You got the bad ending."
    "Next time, maybe you should pursue a relationship."
    "This game is kinda called 'Star Wars Dating Sim,' you know. Genius."
    return
label meet_r2:
    $ r2meeting = True
    r "Beep?"
    p "Oh, hi. I'm [name]."
    r "Beep."
    p "(Hmm...I thought that I misheard this robot, but he's trying to talk in beeps. I'll just pretend that I know what he's saying.)"
    p "Oh, of course."
    r "Beep."
    p "Indeed."
    p "(I'm not really sure what this infernal contraption is trying to relay to me at all. I'll have to interpret it based on the situation.)"
    r "Beep?"
    menu:
        "Yes":
            r "Beep!"
            p "(He wheeled about in a circle...happily, I think, and then wheeled away.)"
            $ r2points += 1
            jump evening
        "No":
            r "Beep! Beep!"
            p "(He abruptly wheeled away in a huff. That is, if robots had lungs to huff with. Do they...? I'm sure there's one out there that does can.)"
            jump evening

label r2_love:
    p "(I was walking down the hallway after lunch when a famililar figure stopped me. It seems like that happens a lot to me.)"
    r "Beep."
    p "(R2 is getting pretty close to me. Of course, I always have to be sitting down or looking down to see him because he's so short.)"
    p "Hi! What are you doing here?"
    r "Beep! Beep?"
    p "(He might have said something seductive, and then asked me what I was doing.)"
    p "Oh, you know, the usual. Just getting things out of my locker and deciding what to do for elective today."
    r "Beep!"
    p "(He's moved behind my legs and is starting to push me. I'd fall over if my feet weren't made of steel.)"
    p "Ok, ok, I'm moving here."
    r "Beep."
    p "(With the beeping guidance coming from behind, I was forced to march through the hall and down the stairs to the basement.)"
    p "Would you mind slowing down a little?"
    r "Beep!"
    p "(He didn't slow down. The whirring sound of his 'feet' became louder as his ramming into my legs became more frequent.)"
    p "Fine, then."
    p "(Just as we were nearing the end of the hallway, I started taking slower steps.)"
    r "Beep! Beep!"
    p "(Is he trying to use a laser on my legs? It's...getting hotter.)"
    p "(Not wanting my legs to be roasted again, I started walking again. R2 beckoned for me to open the door to the computer lab.)"
    p "(I actually hadn't been in the computer lab before today. It was completely empty, but filled to the brim with old-looking computers.)"
    p "(Come to think of it, since when was there a computer lab? I certainly haven't heard of any classes being held here, and there's a printer in the teacher's lounge to satisfy all printing needs.)"
    p "(Now, I'm being nudged towards one of the screens. I sat down in the surprisingly comfortable chair and looked at the screen.)"
    p "(To my surprise, one word popped up on the screen. It said, 'Hello.' I looked over at R2.)"
    p "Did you do this?"
    r "Beep."
    p "(I looked back at the bright screen. Now, it also said, 'Yes.')"
    p "How did you find the computer lab?"
    r "Beep."
    p "Now the screen said, 'You can finally speak to me, and the first thing you ask is about this place?'"
    p "Yup! Come on, I'm curious. I've been going to this school for a few months now, and in all of the school-wide tours, I've never heard any mention of this place. I assumed it was a janitor's closet or something."
    r "Beep..."
    p "The screen was filled with new words. 'I was looking for a power source, and found these, all covered in dust.'"
    p "(I looked around. I hadn't noticed before, but the place was dusty, and smelled faintly of mildew. There were some posters, but I don't think time was kind to them. Most letters were illegible.)"
    p "When did you find this place?"
    r "Beep!"
    p "(The screen read, 'About a week ago.')"
    p "(Hm...I doubt I'm learning the full truth here, but I'll roll with it. This guy has been enrolled at this school for a while, I've heard.)"
    p "(He obviously can't do anything about the dust and posters, but on the tiled floor, there isn't dust like there should be.)"
    p "Oh, ok then. Well, thanks for getting me down here."
    r "Beep."
    p "(The screen read, 'Anything to speak with you.')"
    p ""
label r2_death:
    p "(R2 called me down to the computer lab. School just ended for today, and I have nothing else to do, so I began my descent down to the lab.)"
    p "(It was then that I realized I'd never been in the basement alone. It was lonely when there was nobody murmuring in the hallway or any robot to push me along.)"
    p "(At least the lights were still on, though. It would be terrifying if the lights were off.)"
    p "(Well, here I am. I'd hate to keep R2 waiting.)"
    p "(I opened the door, which opened almost silently, and then flicked on the lights.)"
    p "(Without the beeping and whirring that R2 makes, the computer lab was dead quiet. The sleeping computers didn't make a sound.)"
    p "(I'm not sure how long I waited around for, but it was at some point that I thought I heard a click.)"
    p "(After a little bit longer, I decided that I'd try peeking out to the hallway to see if anyone was there. If not, then I was about ready to give up and go home.)"
    "possible spoopy background music, if can't find anything try fnaf"
    p "(I tried the door, but now it was locked. Since when did classrooms have locks on the outside, and not the inside? My body went cold. How would I get out?)"
    p "(As it was a basement classroom, there were no windows. I opened the closet concealed in one corner of the room.)"
    p "(Now, I was really getting scared. There was no way I could force the door open, and the closet was nothing but dusty cables.)"
    p "(The click made sense now. I realized that somebody had to lock me in. There was no other explanation.)"
    p "(But who? The only person who knew we would meet was R2...no. He wouldn't lock me in here on purpose. It has to be a mistake.)"
    p "(Could it be...Han? He couldn't, either, but I need to believe somebody did it. Was it...)"
    menu:
        "Han Solo":
            p "(It has to be him. Maybe he caught wind of our meeting and got jealous?)"
            $ handidit = True
        "R2D2":
            p "(It has to be him. He was the only one who knows about the computer lab, and the one who told me to come down here. Only someone who had been here before would know that the door locks from the outside.)"
            $ r2didit = True
    p "(I know now who locked me in here. They're going to pay for it.)"
    "transition"
    $ day += 1
    p "(My head is throbbing, and my legs seem like they'll give way at any moment. Missing dinner hasn't affected me as much as not having any water and the stress of possibly dying in here.)"
    p "(I hear footsteps. Is someone here to rescue me? No, they aren't...lockers are opening and closing. They're just here for books and class, unaware that I could be on the verge of my demise.)"
    p "(It's terrifying. I've already been sweating all night, until at some point I must have somehow fallen asleep after desperately trying to break the door open.)"
    p "(Am I crying? I might be, but I can't tell at this point. Please, let me out. Let me out, please. Please.)"
    p "(Ok, I'm definitely sobbing. I can't control myself anymore - each time I breathe out, I'm making a high-pitched squeal of some sort.)"
    p "(I hear fast steps down the hall. Very fast. Is someone running? They get close enough to open the door. Please. Open it.)"
    p "(The door is yanked open. I see him, but nothing registers in my mind.)"
    h "[name]! Let's get out of here. I'm sorry I couldn't find you earlier. No one realized you were missing until R2 casually said you disappeared."
    if handidit = True:
        show black picture
        p "(Now something did. I was hungry and thirsy and angry and not happy and I killed him)"
        p "(I hit him with chair I dug in with my nails he was delicious)"
        p "(I realized)"
        p "(I killed him and ate him)"
        p "(I hit my head on the door, headache was too much)"
        p "(Forehead was getting wet and red and tasty)"
        "You got one of the wrong endings."
        "Do you want some advice? Next time, try making a more logical decision when faced with options."
        return
    p "(It registered with me. He didn't do this. He helped me. It really was R2. I couldn't do anything, though. I kept staring at those blank computer screens. I just couldn't keep my eyes off them.)"
    p "(And then, he was there. Behind Han.)"
    p "(I tried to warn him, but I opened my mouth, and nothing came out.)"
    p "(Suddenly, it was bright and hot. Chairs, carpet, Han, and then myself were burning.)"
    p "(However, all I could do was stare. Even as the air became harder to breathe and I could smell my flesh burning.)"
    "You got one of the wrong endings."
    "At least you guessed correctly. Even so, that didn't change your fate."
    return
label lunch:
    "It's lunch time now. There are still a lot of people I simply don't recognize. Who should I go sit with?"
    if leiameeting == True and r2meeting == True:
        menu:
            "Leia":
                p "(I decided to find Leia. She was with some other people, but still made me feel welcome.)"
                l "Hello, [name]. I'm glad you decided to join us."
                $ leiapoints += 1
                jump afternoon
            "R2":
                p "(I decided to sit with R2. Wait, does he even eat food?)"
                r "Beep."
                $ r2points += 1
                jump afternoon
            "Han Solo":
                jump hansololunch
label leia_love:
    p "lol i luv u"
    l "k"
    "You got one of the good endings. "
# r2 bad end: enter computer lab, get locked in, starve, a guy you're cheating on r2 with saves you, but you're so hungry you eat his flesh and only realize afterwards, then go crazy and bang your head on a window
#inkscape
return
