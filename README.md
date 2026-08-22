# ChatBot 🤖

A rule-based chatbot built in Python, with both a terminal version and a graphical (tkinter) window version.


## Features

`chatbot.py` / `chatbot_window.py` — the original keyword bot from the Month 1 lab guide.

`chatbot_logic.py` / `chatbot_gui.py` — an upgraded version. No API key needed, still 100% rule-based, but:
- Regex pattern matching instead of plain keyword checks (catches more phrasings)
- Basic typo correction ("helo" → "hello")
- Remembers your name and uses it naturally in replies
- Tracks conversation context — notices if you seem down across multiple messages and follows up
- Varied response pools so it doesn't repeat the same line every time
- GUI is a real chat-bubble interface (like WhatsApp/Telegram) instead of a plain text box

## Files
| File | Description |
|---|---|
| `chatbot.py` | Original terminal chatbot + `get_reply()` |
| `chatbot_window.py` | Original basic tkinter window |
| `chatbot_logic.py` | Upgraded rule engine with context, patterns, typo tolerance |
| `chatbot_gui.py` | Upgraded chat-bubble GUI, reuses `chatbot_logic.get_reply()` |

## How to run

**Requirements:** Python 3.10+ (tkinter is included with Python on Windows/Mac)

Recommended:
```bash
python chatbot_logic.py   # terminal
python chatbot_gui.py     # chat-bubble window
```

Original:
```bash
python chatbot.py
python chatbot_window.py
```

## Example
```
Hi! I am ChatBot. What is your name?
You: Sam
Nice to meet you, Sam! Type 'bye' to leave.
Sam: hello
ChatBot: Hey! Good to see you.
Sam: tell me a joke
ChatBot: Why did the programmer quit? They lost their domain!
Sam: bye
ChatBot: Goodbye, Sam!
```

## About
Made as a Month 1 project — first step into building agentic AI applications.