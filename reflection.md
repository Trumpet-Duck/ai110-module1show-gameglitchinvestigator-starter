# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked completely normal when first starting it. Then as I was guessing I noticed the game was giving me incorrect hints. I had then reached my guess limit and tried to start a new game. It would give me a new number but would not actually restart the game and I could not submit a number. I had to refrsh the page if I wanted to play again.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hints given were not correct. It would usally say higher and the number was lower and vice versa. One time it just said lower no matter what number I submitted. 2. When changing the difficulty the number range would never actually change. It would still give a number from 1-100. 3. The new game button would not start a new game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of 80 |"go lower" Hint |"go higher" Hint shown |"none" |
|guess of 30 |"go higher" Hint |"go lower" Hint shown |"none" |
|Range of 1-20, "New Game" button hit |Number of range 1-20 |Number generated "88" |"none" |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude AI
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
The AI noticed that the attempt counting was off by one. This is something I did not notice at first. I verified this by playing the game again and counting the guesses I had made. Then I went into the code and saw the attempt counter started at 1. With both of these pieces of evidece I knew that the AI was correct and fixed it.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI did not give me an incorrect or misleading suggestion. For every bug I gave, it gave a valid suggestion in return. It did what I asked it too and fixed the bugs that I found. I made sure to check the suggestions it gave me and no incorrect ones were given.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed when it passed the test cases and when I saw it work when running the app. This proved that the bug was fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  After adjusting the new game code, I ran the app again to test. I pressed the new game button without doing anything. Then I failed the game to see if the game would restart when pressing "new game" button. After I won the game and pressed the "new game" button. I even changed the difficulty and tested the button. All cases the button worked and a new game was started.
- Did AI help you design or understand any tests? How?
AI did help me design and understand tests. I would ask it for suggestions on what kind of tests I could run. Based on the suggestions it gave me, I combined it with the tests I had come up with to test as much as possible. This made me more confident in the bugs that were fixed.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I dont really undertand too well myself, but I would explain it as streamlit running through the code to update everything with the game and saving the things you input / click to memory.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I would want to reuse is making sure to come up with multiple good test cases. This will slowly help my mind sharpen by being able to think of multiple cases. This would also help me ensure my code is working as intendid.
- What is one thing you would do differently next time you work with AI on a coding task?
I would ask it more questions. There were times where I was trying to understand something by breaking it down in my mind. The issue is that it would take me a long time. I forget that I can ask AI to help break it down for me and help me understand.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I always thought of AI generated code as very buggy and that it would never be useful. But know I realized that it can be useful and it can have bug free code. You just need to give the right prompts and be in control of what you code and what information you give it. It can be very helpful.
