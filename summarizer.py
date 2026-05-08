import os
import sys
import argparse
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()


def build_prompt(transcript):
    return f"""You are a hiring assistant reviewing a real interview transcript. Based only on what is said in the transcript, produce a structured summary with the following three sections:

## Topics Covered
List the main themes and topics discussed as bullet points. Be specific — instead of "technical skills", write something like "state management with RxJS and NgRx". Aim for 4–8 bullet points.

## Profile
On the first line, state the role and seniority level (e.g., "Frontend Engineer — mid-level" or "Operations/Program Manager — mid-senior"). On the next 1–2 sentences, briefly justify your assessment using specific evidence from the transcript.

## Candidate Summary
Write a 3–6 sentence paragraph covering: their background and experience, their strengths (professional or technical), any notable concerns or gaps observed, and your overall impression. Keep it honest and grounded in the transcript — don't speculate beyond what's shown.

If any section cannot be reasonably determined from the transcript, say so in a single sentence.

---
TRANSCRIPT:
{transcript}
"""


def main():
    parser = argparse.ArgumentParser(description="reads a transcript file and prints a structured interview summary")
    parser.add_argument("transcript_file", help="path to the transcript .txt file")
    parser.add_argument("--output", help="save output to a file instead of printing it")
    args = parser.parse_args()

    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY not set. Add it to your .env file.")
        sys.exit(1)

    try:
        with open(args.transcript_file, "r", encoding="utf-8") as f:
            transcript = f.read()
    except FileNotFoundError:
        print(f"Error: File '{args.transcript_file}' not found.")
        sys.exit(1)

    client = Mistral(api_key=api_key)

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "user", "content": build_prompt(transcript)}
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Summary written to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
