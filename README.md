## :space_invader: About

This is a Python script that generates a README file for a given Python code file. 

It does this by first summarizing the code using OpenAI's GPT-3 language model. It then reads in any dependencies required by the code, either from a `requirements.txt` file or by parsing the `import` statements in the code. 

The script then uses OpenAI's API to infer how the code should be run in the terminal and adds this to the README. It also checks if any environment variables are used in the code, and if so, adds them to the README. 

Finally, the script generates the README file and saves it to disk. The user can then share the code and the generated README with others.

## :wrench: Requirements

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```
## :rocket: OpenAI API

This application uses the OpenAI API. You will need to obtain an API key from the [OpenAI website](https://openai.com/), and add it to your environment variables or a .env file in the project root with the key `OPENAI_API_KEY`.

## :shipit: Environment Variables

This application uses the following environment variables, which need to be added to a .env file in the project root:

- OPENAI_API_KEY


## :runner:  Usage

python main.py <file_path>

## :raising_hand: Contribution

All contributions are welcome! Please open an issue or submit a pull request.

