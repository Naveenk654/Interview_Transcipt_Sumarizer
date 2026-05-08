# Prompt Iterations

Tested each version on both transcripts. Transcript 1 is a frontend/mobile dev interview (Prasanna Kumar), transcript 2 is a program management/ops interview (Krishna). Pretty different in style and role type, which is why I used both — I wanted to make sure the prompt didn't just work for one of them.

---

## Iteration 1

### The Prompt

```
You are a hiring assistant. Read the interview transcript below and give me:

1. Topics covered — the main themes discussed
2. Profile — what role and seniority level this candidate fits, with a brief reason
3. Candidate summary — a short paragraph about their background, strengths, concerns, and overall impression

Transcript:
{transcript}
```

### Input (excerpt from Transcript 1)

```
[13:06] Candidate: Hi sir. My name is Prasanna Kumar. I have around nine plus years of experience in software development. My core technical expertise is on Angular, React and Ionic framework. I'm working with the backend by using Node.js, Express and .NET Core.
[13:33] Candidate: I've worked mostly on service-based applications, risk assessment management tools, and communication-based applications. Mainly I focus on Ionic Angular and Ionic Capacitor and Cordova for native functionalities and I deployed applications to iOS and Android. AI assist — Cursor, GitHub Copilot and Claude for the last two years.
...
[55:05] Candidate: Zustand, I cannot use this. I worked on React Query.
[55:14] Interviewer: Can you write an example of Zustand for creating a useStore?
[55:24] Candidate: Yeah. Like a constant. Use store. This is the base structure.
```

### Output

```
### **1. Topics Covered — Main Themes Discussed**
- **Technical Expertise**: Angular, React, Ionic, Node.js, Express, .NET Core, Zustand, React Query
- **Development Experience**: Service-based applications, risk assessment tools, communication apps
- **Mobile Development**: Ionic Capacitor, Cordova, iOS/Android deployment
- **AI Tools**: Cursor, GitHub Copilot, Claude
- **State Management**: Zustand vs. React Query

### **2. Profile — Role & Seniority Level**
**Role:** **Frontend Developer (Mid to Senior Level)**
**Reason:**
- **9+ years of experience** in software development.
- Strong expertise in **Angular, React, and Ionic**, which are widely used in frontend development.
- Experience with **backend technologies (Node.js, Express, .NET Core)** suggests full-stack capabilities.
- Familiarity with **mobile app development (Ionic, Cordova, Capacitor)** indicates versatility.
- Knowledge of **state management (Zustand, React Query)** and **AI tools** shows adaptability.

### **3. Candidate Summary**
Prasanna Kumar is a 9+ year experienced software developer with a strong focus on frontend technologies
(Angular, React, Ionic) and some backend exposure (Node.js, .NET Core). He has worked on service-based
applications, risk assessment tools, and communication apps, deploying them on iOS and Android using
Ionic, Cordova, and Capacitor. His recent work includes AI-assisted development tools (Cursor, GitHub
Copilot, Claude). While he is proficient in React Query, he admits limited experience with Zustand,
which could be a minor gap. Overall, he appears to be a skilled, adaptable developer with a mix of
frontend, mobile, and some backend experience, making him a strong fit for frontend or full-stack roles.
```

### What Worked / What Didn't

The Zustand thing was the most obvious problem. The candidate said straight up he can't use it, then couldn't write the code when asked — but the model listed it as a skill because the interviewer brought it up. So it was reading the question, not the answer. For a hiring tool that's a real issue. On top of that, the topics are too vague and the profile justification is basically just a re-list of what the candidate said about himself at the start. And calling the Zustand gap "minor" is the opposite of what the transcript shows. I ran this on transcript 2 and got the same kind of thing — polite, safe, not something a recruiter could actually use.

---

## Iteration 2

### What I Changed

Added format instructions and gave a contrast example for what "specific" means for topics — like write "Capacitor plugin integration for camera and file system" not just "mobile development." Also broke the summary down into four things it had to cover: background, technical strengths, gaps, overall impression. I was basically trying to make it harder for the model to give a vague non-answer.

### The Prompt

```
You are a hiring assistant reviewing a real interview transcript. Produce a structured summary with exactly these three sections:

## Topics Covered
Bullet points listing the main themes discussed. Be specific — write "Capacitor plugin integration for camera and file system" not just "mobile development". Aim for 5–8 bullets.

## Profile
First line: role and seniority level (e.g. "Frontend Engineer — mid-level").
Next 1–2 sentences: justify with specific evidence from the transcript.

## Candidate Summary
A paragraph of 3–6 sentences. Cover all four of these: (1) background and experience, (2) technical strengths, (3) notable concerns or gaps, (4) overall impression.

Transcript:
{transcript}
```

### Input (same excerpt as Iteration 1, Transcript 1)

Same excerpt used above.

### Output (Transcript 1)

```
## Topics Covered
- AI-powered coding assistance (Cursor, GitHub Copilot, Claude) in development workflows
- Ionic Framework v7 architecture for mobile-first dashboards (responsiveness, performance, lazy loading)
- Capacitor plugin integration for camera and file system (image capture, local storage, sync)
- Tailwind CSS utility-first design system for scalable cross-platform styling
- Angular modular architecture for enterprise dashboards (lazy loading, NgRx, shared services)
- React state management strategy (Context API, React Query, Redux slices)

## Profile
**Full-Stack Mobile Engineer — mid-level**
The candidate demonstrates 9+ years of experience with a strong focus on hybrid mobile development
(Ionic/Angular/Capacitor) and backend integration (Node.js/.NET Core). Their expertise in AI-assisted
development tools (Cursor, Copilot, Claude) and modern frontend frameworks (React, Angular) aligns
well with the role's technical requirements.

## Candidate Summary
Prasanna Kumar brings 9+ years of full-stack development experience, with deep expertise in hybrid
mobile applications using Ionic/Angular and Capacitor for native functionalities. Their technical
strengths include AI-assisted development workflows, scalable UI architectures (Tailwind, modular
Angular), and robust state management strategies (NgRx, React Query). The candidate shows strong
problem-solving skills in system design, particularly in mobile-first dashboards and plugin
integrations (camera/file system). Notable gaps include limited hands-on experience with Zustand
(despite familiarity with Redux) and occasional hesitation in live coding scenarios. Overall, they
present as a technically competent engineer with practical experience in modern web/mobile development
stacks, though their Redux knowledge appears more theoretical than applied.
```

Big improvement on transcript 1. Topics are useful, Zustand is actually flagged as a gap this time, and the profile says something real. Then I ran the same prompt on transcript 2.

### Output (Transcript 2 — Krishna, same prompt)

```
## Topics Covered
- Fraud detection and prevention unit (FDPU) setup and ISO certification
- End-to-end CRM implementation and integration with credit scoring (Experian, CIBIL) and telecom APIs (Jio, Airtel)
- Vendor onboarding and performance management, including escalation and termination processes
- BPO/calling efficiency improvements through predictive dialing and CRM automation
- KPI tracking for sales teams, including talk time, revenue, and target achievement
- Stakeholder management and prioritization across multiple geographies and departments
- Data presentation and conflict resolution with leadership

## Profile
**Program Manager — mid-level**
The candidate demonstrates mid-level program management experience through their work in fraud
detection, CRM implementation, and vendor management. They have led cross-functional initiatives,
managed vendor relationships, and improved operational efficiency in ed-tech and digital finance domains.

## Candidate Summary
Krishna is a mid-level program manager with a background in operations, fraud detection, and vendor
management, primarily in ed-tech and digital finance. Their experience includes building a fraud
detection unit from scratch, implementing CRM systems, and integrating third-party APIs (credit
scoring, telecom) to automate risk assessment. They have a strong track record in vendor onboarding,
performance tracking, and stakeholder management, with experience presenting data to leadership and
resolving conflicts. Notable strengths include process improvement, cross-functional collaboration,
and analytical problem-solving. However, their communication style — mixing Hindi jargon — may impact
confidence in high-level leadership interactions. Overall, Krishna is a proactive and results-driven
professional with the technical and managerial skills to handle complex program management challenges.
```

### What Worked / What Didn't

Transcript 1 came out well. The problem with transcript 2 was the "technical strengths" wording in the summary instructions — the model picked that up and at the end called Krishna's work "technical and managerial skills." But Krishna's an ops person, his strengths are around process, vendors, stakeholders. Nothing he talked about was engineering work. The word "technical" was baked into the prompt and it quietly pulled the output in the wrong direction. Needed to just remove it.

---

## Iteration 3 (Final)

### What I Changed

Dropped "technical" from the summary section so it doesn't assume a dev candidate. Added a fallback line for cases where the transcript is too short or vague to say anything reliable — I wanted the model to just say so rather than guess. Also reworded the topics instruction slightly so it pulls from what was actually discussed in the interview, not just whatever the candidate mentioned upfront.

### The Prompt

```
You are a hiring assistant reviewing a real interview transcript. Based only on what is said in the transcript, produce a structured summary with the following three sections:

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
```

### Output (Transcript 1 — Prasanna Kumar)

```
## Topics Covered
- AI-assisted coding workflows with tools like Cursor, GitHub Copilot, and Claude
- Ionic Framework architecture, responsiveness, and performance optimization for mobile dashboards
- Capacitor plugin ecosystem for native mobile functionalities (camera, file system, network sync)
- Tailwind CSS design system with utility-first styling and responsive breakpoints
- Angular enterprise application structure with modular architecture, lazy loading, and state management
- React state management strategies (Context API, React Query, Redux slices) for large-scale apps

## Profile
**Frontend Engineer — mid-level**

The candidate demonstrates solid mid-level expertise in frontend frameworks (Angular, React, Ionic) and
backend technologies (Node.js, Express, .NET Core), with 9+ years of experience. Their responses show
practical knowledge of modern tooling (AI assistants, Capacitor) and architectural patterns (modular
design, state management), though their depth in advanced state management tools like NgRx appears
limited compared to Redux.

## Candidate Summary
Prasanna Kumar has nearly a decade of experience primarily focused on frontend development with Angular,
React, and Ionic, complemented by backend work in Node.js and .NET Core. They demonstrate strong
hands-on skills in mobile development (Ionic Capacitor/Cordova), AI-assisted coding workflows, and
responsive design systems using Tailwind CSS. Their architectural approach is methodical, emphasizing
modularity, lazy loading, and reusable components. While they show familiarity with state management
patterns (RxJS, React Query, Redux), their depth in enterprise-grade solutions like NgRx is less
evident. The candidate communicates technical concepts clearly but occasionally struggles with precise
tool-specific implementations (e.g., Zustand code example). Overall, they present as a capable
mid-level engineer with practical, production-ready experience in frontend development and mobile
architectures.
```

### Output (Transcript 2 — Krishna)

```
## Topics Covered
- Fraud detection and prevention in financial operations (e.g., building risk scores, CRM integration, vendor partnerships)
- Vendor management and onboarding processes (e.g., market research, commercial negotiations, performance tracking)
- Process improvement in operations (e.g., CRM adoption, automation, KPI alignment)
- Stakeholder and leadership engagement (e.g., presenting data, handling disagreements, prioritizing initiatives)
- Program management challenges (e.g., cross-team alignment, execution speed, resource allocation)
- Analytics and reporting (e.g., executive dashboards, KPIs, data validation)
- BPO/calling efficiency improvements (e.g., predictive dialing, auto-dialers, time management)

## Profile
**Program Manager — mid-level**

The candidate demonstrates experience in program and operations management, with a focus on fraud
detection, vendor management, and process optimization. Their background includes leading end-to-end
initiatives (e.g., building a CRM, implementing risk scores) and collaborating with leadership
(e.g., CBOs, CXOs), though their communication style (heavy use of Hindi jargon) may need refinement
for high-level stakeholder interactions.

## Candidate Summary
Krishna has a mechanical engineering background but transitioned into operations and program management,
with roles in ed-tech and digital finance. Their strengths include designing and implementing fraud
detection systems (e.g., integrating credit scores, building risk models), improving operational
efficiency (e.g., CRM adoption, predictive dialing), and managing vendors (e.g., onboarding 22
pan-India partners). They have also handled analytics and reporting (e.g., executive dashboards,
KPI tracking) and demonstrated resilience in resolving conflicts (e.g., proving fraud cases to
leadership). Notable gaps include a lack of clarity on their exact role in the target position and
potential communication challenges in high-stakes leadership settings, as noted by the interviewer.
Overall, they appear to be a pragmatic, results-driven candidate with room to refine executive
communication.
```

### Edge Case Test — Transcript Too Vague to Summarize

I also tested on a very short transcript with basically no useful information to see if the model would just make something up or admit it can't say anything:

**Input:**
```
[00:01] Interviewer: Hi, thanks for joining. Tell me a bit about yourself.
[00:09] Candidate: Hi, thank you for the opportunity. I am looking for good roles and want to grow professionally.
[00:22] Interviewer: What kind of work are you interested in?
[00:27] Candidate: I am flexible and open to different kinds of work. I like learning new things.
[00:41] Interviewer: Okay. We will review your profile and get back to you.
[00:45] Candidate: Thank you so much. Have a good day.
```

**Output:**
```
## Topics Covered
- General career interests and flexibility
- Openness to learning new skills

## Profile
**Role and Seniority Level:** Cannot be reasonably determined from the transcript.

## Candidate Summary
The candidate expresses a general interest in professional growth and flexibility in their career path,
emphasizing a willingness to learn new things. However, the transcript provides no details about their
background, experience, technical skills, or specific areas of expertise. Without further information,
it is impossible to assess their qualifications or suitability for any role. The interaction is brief
and lacks substantive discussion.
```

Profile says "Cannot be reasonably determined" instead of guessing, and the summary is honest about there being nothing to work with. That's the right behaviour — in a real pipeline some transcripts are just going to be thin and the tool shouldn't invent detail that isn't there.

### What Worked / What Didn't

Removing "technical" from the summary fixed the transcript 2 issue. Krishna's summary now reads like an ops candidate, not a developer. The Zustand problem from iteration 1 also got handled indirectly — asking the model to stay grounded in the transcript and look for gaps was enough to get it to flag the Zustand struggle without needing an explicit instruction for it. I noticed that looking at the transcript 1 output, it calls out the Zustand example directly in the summary. The edge case also worked the way I wanted — it said it couldn't determine the profile rather than making something up. The thing I'd still want to fix is seniority. The model is going mostly off what candidates say about themselves rather than how they actually performed, and I don't think more instructions will fix that. Probably needs a few worked examples in the prompt.
