# Interview Transcript Summarizer

Script that takes an interview transcript file and prints a structured summary of the candidate — what was discussed, what role they fit, and a short written assessment.

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your API key

Copy `.env.example` to `.env` and paste in your Mistral API key:

```bash
# Mac/Linux
cp .env.example .env

# Windows
copy .env.example .env
```

Open `.env` and replace `your_api_key_here` with your actual key.

### 3. Run the script

```bash
python summarizer.py path/to/transcript.txt
```

To save to a file instead of printing to the terminal:

```bash
python summarizer.py path/to/transcript.txt --output summary.txt
```

### Example

```bash
python summarizer.py Interview_Transcripts/sample_transcript_assignment_1.txt
```

---

## LLM Provider and Model

- **Provider:** Mistral AI
- **Model:** `mistral-small-latest`
- **Temperature:** `0`

I went with Mistral since I already had an API key. `mistral-small-latest` worked fine for this — the task is just reading a transcript and filling in a fixed structure, nothing that needs a bigger model. Temperature is set to 0 so you get the same output every time on the same transcript, which matters when multiple people might be running this on the same candidate.

---

## Reflection

Honestly the biggest surprise was how much exact phrasing matters even for something this simple. My first attempt just said "give me the topics, profile, and summary" and the output was technically correct but useless — everything came back vague and safe, like the model was writing a reference letter instead of an assessment. I had to be pretty specific about what I actually wanted before it started saying anything real.

The thing that caught me was a wording issue in version 2. Writing "technical strengths" in the summary instructions was fine for the software dev transcript, but when I ran the same prompt on the ops/PM transcript, the model started describing things like CRM rollouts and fraud dashboards as technical strengths — which just felt wrong. That's operational work. One word change fixed it but I only caught it because I tested on both transcripts. If I'd only used one I would have missed it.

With more time I'd add a worked example directly in the prompt — an input/output pair showing what a good summary actually looks like — because right now the length and tone vary a bit depending on how much the transcript gives you. I'd also look more at seniority. Right now the model goes off what the candidate claims about their experience, not what they actually showed in the interview. You can partially fix this by asking for gaps and concerns, but it's not fully solved. Probably needs examples more than instructions.
