import requests

parameters = {
    "amount":10,
    "type": "boolean",
    "category": 18,
}

response = requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]






# question_data = [
# {
# "type": "multiple",
# "difficulty": "easy",
# "category": "General Knowledge",
# "question": "The likeness of which president is featured on the rare $2 bill of USA currency?",
# "correct_answer": "Thomas Jefferson",
# "incorrect_answers": [
# "Martin Van Buren",
# "Ulysses Grant",
# "John Quincy Adams"
# ]
# },
# {
# "type": "multiple",
# "difficulty": "easy",
# "category": "General Knowledge",
# "question": "What is &quot;dabbing&quot;?",
# "correct_answer": "A dance",
# "incorrect_answers": [
# "A medical procedure",
# "A sport",
# "A language"
# ]
# },
# {
# "type": "multiple",
# "difficulty": "easy",
# "category": "General Knowledge",
# "question": "What is the profession of Elon Musk&#039;s mom, Maye Musk?",
# "correct_answer": "Model",
# "incorrect_answers": [
# "Professor",
# "Biologist",
# "Musician"
# ]
# },
# {
# "type": "multiple",
# "difficulty": "medium",
# "category": "General Knowledge",
# "question": "What year was the first Apple iPod introduced?",
# "correct_answer": "2001",
# "incorrect_answers": [
# "2000",
# "1999",
# "1998"
# ]
# },
# {
# "type": "multiple",
# "difficulty": "easy",
# "category": "General Knowledge",
# "question": "How many furlongs are there in a mile?",
# "correct_answer": "Eight",
# "incorrect_answers": [
# "Two",
# "Four",
# "Six"
# ]
# },
# {
# "type": "multiple",
# "difficulty": "easy",
# "category": "General Knowledge",
# "question": "When someone is inexperienced they are said to be what color?",
# "correct_answer": "Green",
# "incorrect_answers": [
# "Red",
# "Blue",
# "Yellow"
# ]
# },
# {
# "type": "boolean",
# "difficulty": "medium",
# "category": "General Knowledge",
# "question": "The vapor produced by e-cigarettes is actually water.",
# "correct_answer": "False",
# "incorrect_answers": [
# "True"
# ]
# },
# {
# "type": "boolean",
# "difficulty": "medium",
# "category": "General Knowledge",
# "question": "Fast food restaurant chains Carl&#039;s Jr. and Hardee&#039;s are owned by the same company.",
# "correct_answer": "True",
# "incorrect_answers": [
# "False"
# ]
# },
# {
# "type": "multiple",
# "difficulty": "easy",
# "category": "General Knowledge",
# "question": "Which American-owned brewery led the country in sales by volume in 2015?",
# "correct_answer": "D. G. Yuengling and Son, Inc",
# "incorrect_answers": [
# "Anheuser Busch",
# "Boston Beer Company",
# "Miller Coors"
# ]
# },
# {
# "type": "multiple",
# "difficulty": "easy",
# # "category": "General Knowledge",
# # "question": "The New York Times slogan is, &ldquo;All the News That&rsquo;s Fit to&hellip;&rdquo;",
# # "correct_answer": "Print",
# # "incorrect_answers": [
# # "Digest",
# # "Look",
# # "Read"
# # ]
# }
# ]
