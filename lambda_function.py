import json
import random

def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))

    # Credit for jokes: https://punandjokes.com/python-jokes/
    jokes = [
        "Why did the Python developer go broke? Because he used up all his inheritance!",
        "Why don't Python programmers like to fight dragons? Because they don't like dynamically-typed languages.",
        "What do you get when you cross a Python with a Cobra? A syntax error!",
        "Why do Python programmers prefer snake_case? Because they don't like Java.",
        "What's a Python's favorite subject in school? Hisss-tory!",
        "How do you comfort a JavaScript bug? You console it.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
        "What do you call a group of musical whales? An orca-stra!",
        "Why do Python programmers prefer MacBooks? Because they don't need a right-click.",
        "Why did the Python programmer put on a jacket? Because he wanted to catch an exception!",
        "What's a Python's favorite type of sandwich? A wrapper.",
        "Why do Python developers prefer Monty Python? Because they appreciate a good 'Life of Brian'.",
        "What do you call a Python program that keeps running forever? A snake loop!",
        "Why did the Python developer get rejected by their crush? Because they had no class!",
        "Why do Python programmers never tell lies? Because they can't 'true'st each other.",
        "What did one Python package say to another? 'Don't worry, I've got your back!'",
        "Why do Python programmers love nature? Because it has no runtime errors.",
        "Why did the Python developer go broke? Because he couldn't find his namespace!",
        "What do you call a Python script that's been run by a cat? A scratch program.",
        "Why don't Python programmers like to use all caps? Because they don't want to shout in code!",
        "What do you get when you cross a computer and a lifeguard? A screensaver.",
        "Why did the Python developer always carry a pencil? In case they made a typo!",
        "Why did the Python developer go broke? Because they couldn't account for their variables.",
        "Why was the Python developer always calm under pressure? Because they had good exception handling!",
        "Why was the Python developer bad at math? Because they couldn't find Pi.",
        "Why was the Python programmer always in a good mood? Because he had plenty of 'list' to be happy!",
        "What do you call a snake that's 3.14 meters long? A π-thon!",
        "How do you know if a Python developer likes you? They'll always return your calls.",
        "Why did the Python developer break up with his keyboard? Because he felt it wasn't giving him enough space.",
        "Why don't Python programmers play hide and seek? Good luck hiding when you can't even find your own code!"
    ]

    return {
        'statusCode': 200,
        'body': json.dumps({ 'message': random.choice(jokes) })
    }