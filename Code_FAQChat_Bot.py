import difflib

# Predefined WBJEE FAQs
faq_data = {
    "what is wbjee": "WBJEE (West Bengal Joint Entrance Examination) is a state-level entrance exam for admission to engineering, pharmacy, and architecture courses in West Bengal.",
    "who conducts wbjee": "WBJEE is conducted by the West Bengal Joint Entrance Examinations Board (WBJEEB).",
    "what is the eligibility for wbjee": "Candidates must have passed 10+2 with Physics and Mathematics along with Chemistry/Biology/Biotechnology/Computer Science and must secure at least 45% marks (40% for reserved categories).",
    "what is the exam pattern of wbjee": "WBJEE has two papers: Paper 1 (Mathematics) and Paper 2 (Physics & Chemistry). Each paper has MCQs with different marking schemes.",
    "what is the syllabus of wbjee": "The WBJEE syllabus includes Physics, Chemistry, and Mathematics from the 10+2 level.",
    "how many questions are asked in wbjee": "There are 155 questions in total: 75 in Mathematics and 40 each in Physics and Chemistry.",
    "what is the marking scheme of wbjee": "There are 3 categories of questions with +1, +2, and +2 marks, with negative marking for wrong answers in some categories.",
    "what is the mode of wbjee": "WBJEE is conducted in offline mode (OMR-based pen and paper test).",
    "when is wbjee conducted": "WBJEE is usually conducted once a year, around April or May.",
    "how to apply for wbjee": "You can apply online through the official WBJEEB website by filling out the application form and paying the fee.",
    "what is the application fee for wbjee": "The fee is ₹500 for General category and ₹400 for SC/ST/OBC candidates (subject to change each year).",
    "what is the duration of wbjee": "The exam consists of two papers of 2 hours each, conducted on the same day.",
    "exit": "Thanks for using the WBJEE FAQ Chatbot. Goodbye!"
}

def chatbot_response(user_input):
    questions = list(faq_data.keys())
    # Find closest matching question
    match = difflib.get_close_matches(user_input.lower(), questions, n=1, cutoff=0.5)
    
    if match:
        return faq_data[match[0]]
    else:
        return "Sorry, I don’t have information about that. Try asking another WBJEE-related question."

# Main loop
print("🤖 WBJEE FAQ Chatbot (CodeAlpha Task 2)")
print("Ask me anything about WBJEE! (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot:", faq_data["exit"])
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
