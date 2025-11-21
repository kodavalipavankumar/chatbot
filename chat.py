import os
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables from .env file
load_dotenv()

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OPENAI_API_KEY.")
        sys.exit(1)

    # Initialize the ChatOpenAI model
    try:
        chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    except Exception as e:
        print(f"Error initializing ChatOpenAI: {e}")
        sys.exit(1)

    print("Welcome to the LangChain Chat! (Type 'exit' or 'quit' to stop)")
    
    messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            messages.append(HumanMessage(content=user_input))
            
            print("AI: ", end="", flush=True)
            response = chat.invoke(messages)
            print(response.content)

            messages.append(response)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
