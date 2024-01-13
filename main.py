from openai import OpenAI

age = input("What is your age? (Enter a number) ")
license = input("Do you have a driver's license (and car)? [Y/N] ")

if(license == "y" or license == "Y"):
    license = "has a car and license"

else:
    license = "does not have a car and license"

education = input("What is your level of education? (Examples: high school, university, PhD, etc.) ")
languages = input("Do you speak multiple languages? ")

if(languages == "y" or languages == "Y"):
    languages = "does speak multiple languages"

else:
    languages = "does not speak multiple languages"

animalComfort = input("Are you comfortable with animals? [Y/N] ")

if(animalComfort == "y" or animalComfort == "Y"):
    animalComfort = "is comfortable working with animals"

else:
    animalComfort = "is uncomfortable with animals"

childrenComfort = input("Are you comfortable with caring for children? [Y/N] ")

if(childrenComfort == "y" or childrenComfort == "n"):
    childrenComfort = "is comfortable taking care of children"

else:
    childrenComfort = "is not comfortable working with children"

seniorCare = input("Are you comfortable taking care of seniors citizens? [Y/N] ")

if(seniorCare == "y" or seniorCare == "Y"):
    seniorCare = "is comfortable taking care of elderly citizens"

else:
    seniorCare = "is not comfortable taking care of elderly citizens"

havePhone = input("Do you have a phone? [Y/N] ")

if(havePhone == "y" or havePhone == "Y"):
    havePhone = "does have a phone"

else:
    havePhone = "does not have a phone"

location = input("Where do you live? (City, State Country) ")

remoteWorkplace = input("Do you prefer to work remotely? [Y/N] ")
if(remoteWorkplace == "y" or remoteWorkplace == "Y"):
    remoteWorkplace = "prefers working online"

else:
    remoteWorkplace = "does not prefer to work at home"


# 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
# Next section uses chatGPT to find the best job for the person based on their inputs.

client = OpenAI(api_key="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")

messages = [{"role": "system", "content" : "What is the best occupation for a person that is " + age + " years old, lives in " + location + ", has only " + education + ", " + childrenComfort + ", "  +  license + ", " + languages + ", " + animalComfort + ", " + seniorCare + ", " + havePhone + ", " + remoteWorkplace + ", and does not have a strong financial situation. Give just a list of professions with explanations"
}]

completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

chat_response = completion.choices[0].message.content

print("")
print("The best jobs for you are: ")
print("")
print(chat_response)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Sample prompt to be sent to the HTML page
    prompt = "Enter your text:"

    # Render the template and pass the prompt
    return render_template('index.html', prompt=prompt)

@app.route('/process_input', methods=['POST'])
def process_input():
    # Retrieve text input from the HTML form
    user_input = request.form['user_input']

    # Process the input (you can perform any desired logic here)

    # Send a response back to the user (for demonstration purposes, echoing the input)
    return f"You entered: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)

