# restaurant-finder
A chatbot to find restaurant based on location and cuisine(s) using Python3 and ZomatoAPI


#### What is Chatbot?

A chatbot is a an Artificial Intelligence developed piece of software to gauge consumer’s needs and then assist them to perform a particular task like a commercial transaction, hotel booking, form submission etc . Today almost every company has a chatbot deployed to engage with the users. Some of the ways in which companies are using chatbots are:

- To deliver flight information
- To connect customers and their finances
- As customer support

The possibilities are (almost) limitless.


#### How do Chatbots work?

There are broadly two variants of chatbots: Rule-Based and Self-learning.

- In a Rule-based approach, a bot answers questions based on some rules on which it is trained on. The rules defined can be very simple to very complex. The bots can handle simple queries but fail to manage complex ones.

- Self-learning bots are the ones that use some Machine Learning-based approaches and are definitely more efficient than rule-based bots. These bots can be of further two types: Retrieval Based or Generative

i) In retrieval-based models, a chatbot uses some heuristic to select a response from a library of predefined responses. The chatbot uses the message and context of the conversation for selecting the best response from a predefined list of bot messages. The context can include a current position in the dialogue tree, all previous messages in the conversation, previously saved variables (e.g. username). Heuristics for selecting a response can be engineered in many different ways, from rule-based if-else conditional logic to machine learning classifiers.
ii) Generative bots can generate the answers and not always replies with one of the answers from a set of answers. This makes them more intelligent as they take word by word from the query and generates the answers.


#### How to design Chatbot?

Link- https://docs.google.com/document/d/1r_fHwzD141LCXd7pjf5lnXUW4QE4gb5mNY9-6nOFxsg/edit?usp=sharing

There are multiple ways to develop chatbot mainly Natural Language Processing and Machine Learning is used. 



# Restaurant-Finder:

Problem Statement: Develop a software which can find/suggest restaurants based on preference of location and cuisine using Python3 and ZomatoAPI.

To check this prototype: Download and run the restaurant_bot.py on any Python IDLE in your local system. 

## How to developed it?

1) Get an access code of Zomato API: 

- Log in or create a free account on Zomato.
- Navigate to their developers page and click on the “Generate API Key” button. The API requires that you enter your phone number and Company Website/Blog.

Documentation: https://developers.zomato.com/documentation

Note: To use any function from the developers page, enter the details required for that function and get an url, which will help you in fetching data from the page. 

2) Code:

Open Python IDLE and using access code and url write functions and data which are required for the software. In this prototype, the user will enter the location and cuisine(s) and the software will find restaurants. So to find restuarants, the location details (entity_id and entity_type) are required and then the restuarants would be suggested and then from that data restuarant name, address, cuisines, ratings, and url are found. 

The code is well documented in the .py file. 


#### Limitations:

- It can be implemented using NLP for better results and understanding variations in user's input.
- Can be deployed using SlackAPI or on Whatsapp as it is just a prototype. 


To know more about chatbot development (for beginners) :

- https://medium.com/swlh/end-to-end-chatbot-using-sequence-to-sequence-architecture-e24d137f9c78
- https://medium.com/voiceui/conversational-ai-how-do-chatbots-work-4f1bfd069013



































