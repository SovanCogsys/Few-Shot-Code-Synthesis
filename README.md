🧠 Few-Shot Code Synthesis for MCQ-Based Assessment
This project demonstrates how to leverage OpenAI's GPT-4o for few-shot prompting to automatically generate Python code templates for multiple-choice questions (MCQs). Given a static MCQ as input, the system returns executable Python code that:

Randomizes key parameters (e.g., numbers, names, structures),

Computes the correct answer programmatically,

Generates plausible distractors,

Outputs the question, options, and correct answer in a structured format.

🔍 Key Features
🧠 Few-Shot Prompting: Uses structured example-based prompts to guide GPT-4o in code generation.

🧮 Executable Output: Each generated script can be run to create multiple randomized versions of the same question.

🧰 Support for Logic & Math: Handles arithmetic, permutations, primality, counting problems, and more.

📦 Ready for Integration: Outputs are formatted for use in MCQ engines or educational platforms.

📂 Structure
main.py: Entry point for user input and API invocation.

prompts/: Stores system and user prompts used in few-shot examples.

examples/: Sample generated Python files from GPT-4o.

outputs/: Stores generated MCQs and answer keys.

⚡ Example
Input:
How many five-digit prime numbers can be formed using the digits 1, 2, 3, 4, and 5 without repetition?
Output:
A Python script that:

Uses itertools.permutations to generate all permutations,

Filters primes with a custom is_prime() function,

Returns a count and formatted MCQ.
