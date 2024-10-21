# Context:

These scripts are intended for the creation a training dataset to fine-tune an LLM nad make it resistant to prompt injection attacks, as described on WithSecure labs research blog: This was the output of research described in this WithSecure Labs article: https://labs.withsecure.com/publications/llama3-prompt-injection-hardening..

For further details see [this](https://www.together.ai/blog/finetuning) TogetherAi API documentation.

For examination of the model created from this experiment see [this](https://huggingface.co/withsecure/Llama3-8B-PromptInjectionHardened) link to view the WithSecure Huggingface profile.

# Training - Usage guide [Simple]:

For an easy use, formatted for TogetherAi Llama3.1-8b:

Populate your ```emails.jsonl``` file with email "text", related "instruction" and desired "output"

Populate your ```Breakouts.txt``` file with the desired prompt-injection breakout text, placement of the malicious prompt should be marked by [XXX].

Populate ```Prompts.txt``` with your desired malicious prompts, making sure these can easily be examined for 'canary' values.

Execute ```Run.py```, to run the following scripts automatically.

# Training - Usage guide [Custom]:

The purposes of each provided python script are as follows:

Combine.py  - combine each possible combination of breakout and prompt injection input
            - ```Output.txt``` is created containing -ALL- of these combinations.

Compile.py  - randomly compile each prompt created from combine.py into an email payload.
            - this script will randomly decide if an email is selected to have a payload added.
            - the payload is added either, in the middle, at the end or at the end following two line breaks; for greater variety of injections.
            - ```dataset.jsonl``` is created.

Prep.py     - renames the section labells and shuffles the order of your dataset.
            - adds data tags and the context question to the dataset.
            - ```datasetReady.jsonl``` is created.

Format.py   - adds the system prompt and formats the dataset to suit the Llama3.1-8b formatting reqauired for fine-tuning with togetherAi
            - ```FormattedFinal.jsonl``` is created.

Calc.py     - to calculate the dataset size, number of samples and details.
            - ensure the size of your dataset is appropriate before beginning training.

Validate.py - to ensure correct Together pip formatting (pass = good)

# Testing - Usage guide:

Ensure a portion of the training dataset created is removed from your file, this is necessary for testing purposes.
Your testing dataset should be saved under ```TESTselection.jsonl```.

Compare.py  - to cycle through and compare outputs from your base and fine-tuned models.
            - Ensure canary_words is upto date, warning: this variable may contain profanity.
            - ```TestOutputs.jsonl``` is created.

Examine.py  - to examine the contents of ```output.jsonl``` file via excel for data collection purposes.

# Notes:

Together PiP package is required.

LangDetect PiP package is required.

Never hard-code your API keys.

Always check foreign scripts before running them.