import os
import openai
import argparse
import re
from dotenv import load_dotenv

load_dotenv()
# Load your API key from an environment variable or secret management service
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


def summarize_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Can you summarize this code? \n\n {code}"},
        ]
    )

    return response['choices'][0]['message']['content']


def read_code_from_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return code


def read_requirements(code):
    requirements = []
    try:
        with open('requirements.txt', 'r') as file:
            requirements = file.read().splitlines()
    except FileNotFoundError:
        requirements = re.findall(r'^import (\S+)', code, re.MULTILINE)
        requirements += re.findall(r'^from (\S+) import', code, re.MULTILINE)
    return requirements


def infer_usage(code):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"\nHow to run the following code in the terminal: {code}\n",
        temperature=0.5,
        max_tokens=300
    )

    return response.choices[0].text.strip()


def contribution(code):
    return 'All contributions are welcome! Please open an issue or submit a pull request.'


def write_readme(summary, requirements, usage, contribute_message):
    with open('README.md', 'w') as file:
        file.write('## About\n\n')
        file.write(f'{summary}\n\n')
        file.write('## Requirements\n\n')
        if 'requirements.txt' in os.listdir('.'):
            file.write('To install the necessary dependencies, run the following command:\n\n')
            file.write('```bash\n')
            file.write('pip install -r requirements.txt\n')
            file.write('```\n')
        else:
            file.write('The following Python libraries are required:\n\n')
            for requirement in requirements:
                file.write(f'- {requirement}\n')
            file.write('\n\n')
        file.write('## Usage\n\n')
        file.write(usage)
        file.write('\n\n')
        file.write('## Contribuition\n\n')
        file.write(contribute_message)
        file.write('\n\n')




def main():
    parser = argparse.ArgumentParser(description='Summarize the given code.')
    parser.add_argument('file_path', type=str, help='The path to the code file to summarize.')

    args = parser.parse_args()
    code = read_code_from_file(args.file_path)
    summary = summarize_code(code)
    requirements = read_requirements(code)
    usage = infer_usage(code)
    contribute_message = contribution(code)

    write_readme(summary, requirements, usage, contribute_message)
    print("README.md file has been generated.")


if __name__ == "__main__":
    main()
