---
name: crisis-response
description: >
  Use this skill whenever the brand is facing an urgent issue, PR crisis, service disruption,
  data incident, or negative publicity, and needs to draft communication playbooks, holding
  statements, internal FAQs, or stakeholder notifications. Trigger on requests like "we need a
  crisis statement", "draft a holding statement for this incident", "write an internal talking
  points memo about X", "how do we respond to this negative news", or "create a stakeholder FAQ
  for a service outage". Handles swift, highly strategic communication framing.
---

# Crisis Response

Drafts strategic crisis communication materials including holding statements, press responses,
internal talking points, and stakeholder Q&A sheets. Prioritizes reputational protection, clarity,
transparency, and compliance guidelines. Produces a structured `.md` crisis response plan saved in `output/pr/`.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Context.md` — company profile, executive leadership team, standard descriptors
- `_context/Brand_Voice_Guide.md` — guidelines for formal corporate voice (crisis communications must be exceptionally objective, empathetic, and serious; eliminate all marketing taglines or sales language)

## Clarify inputs first

Confirm with the user:
1. **The Incident / Crisis:** What happened, when did it occur, and who is affected?
2. **Known Facts:** What metrics, numbers, or details are confirmed (and what is still unconfirmed)?
3. **Primary Stakeholders:** Who needs updates? (Customers, partners, employees, shareholders, media)
4. **Current Status & Resolution Steps:** What is the company doing *right now* to address or investigate the issue?
5. **Timeline:** When must these statements be ready or released?

If the user's request makes these inputs clear, skip asking and proceed.

## Workflow

### Step 1 — Position & Empathy Mapping
Map out the company's communication stance:
- **Acknowledge:** State what has happened clearly, without obfuscation.
- **Empathize:** Acknowledge impact on users/stakeholders immediately.
- **Act:** Outline remediation actions and resolution timelines.
- **Investigate:** State what steps are being taken to prevent recurrence.
- **Avoid:** Do not shift blame, use corporate jargon, or make speculative assertions.

### Step 2 — Draft the Holding Statement (Immediate Use)
Create a short (max 100 words) statement for media or social media inquiries to buy time while details are confirmed:
- State what is known.
- Detail immediate response actions.
- Provide a timeline for the next update.

### Step 3 — Draft the Full Response Statement (Press/Public Release)
Create a comprehensive response detailing facts, corrective measures, and leadership quotes.

### Step 4 — Internal talking points & FAQ
Draft internal guidelines for staff to ensure consistent messaging across all channels.

## Output structure (`.md`)

Save as `output/pr/crisis-playbook-<topic>-<date>.md` with this exact structure:

```
# Crisis Response Playbook: [Incident Title]
Date: [yyyy-mm-dd]
Incident Type: [e.g., Outage / Security Incident / Executive Change]
Approval Status: [DRAFT - PENDING LEGAL & EXECUTIVE SIGN-OFF]

## Executive Summary
[Brief recap of the incident, impact scope, and the primary communication strategy.]

---

## 1. Immediate Holding Statement
*For use in response to direct incoming media or customer inquiries during the first 1-4 hours.*

```text
[INSERT HOLDING STATEMENT - Max 100 words. Factual, brief, commits to update timeline.]
```

---

## 2. Public Statement / Press Release
*For dissemination once key facts are confirmed.*

**[CITY, STATE] — [Month Day, Year]** — [Company Name] today released the following statement regarding [Incident].

"Insert quote from CEO or Chief Operations Officer," said [Name], [Title]. "Quote must express sincere apology, describe immediate remediation actions, and state the company's commitment to core values."

[Describe the incident parameters - what is confirmed. Do not guess.]
[Detail the remediation steps: Step 1, Step 2, Step 3.]
[Provide support contact information or links for affected users.]

---

## 3. Internal Talking Points & Staff Guidelines
*Crucial: Do not distribute externally. For customer-facing teams (Support, Sales, AMs).*

### Key Rules
1. Refer all media inquiries to [Media Contact Name] at [Media Contact Email]. Do not improvise.
2. Limit discussions to confirmed facts. Do not speculate on root cause or liability.
3. [Insert voice rule: e.g., Be empathetic, patient, and focus on resolution.]

### Approved Customer Responses
- **Customer Query:** "What happened to my service?"
  - **Approved Answer:** "[Empathy statement]. We experienced a service disruption at [Time]. Our team resolved the issue by [Time] and all systems are now fully operational. We apologize for the inconvenience."
- **Customer Query:** "Was my data exposed?"
  - **Approved Answer:** "Our team is conducting a thorough investigation. At this time, we have no evidence that customer data was compromised. We will provide updates immediately if our findings change."

---

## 4. Press Q&A Document
*Prep document for spokespeople handling hard journalist questions.*

- **Question:** "Who is to blame for this failure?"
  - **Approved Response:** "Our focus right now is entirely on resolving the issue for our customers and ensuring system stability. We take full responsibility for our services and are investigating the root cause to ensure this does not happen again."
- **Question:** "What is the financial impact of this outage?"
  - **Approved Response:** "We are currently focused on restoring operational integrity. We will assess business impacts in due course, but our immediate priority is customer support."
```

## Quality checklist

- [ ] All statements are exceptionally objective, empathetic, and serious in tone
- [ ] No marketing taglines or promotional copy present anywhere in the file
- [ ] Direct quotes attributed to correct executives and marked for client sign-off
- [ ] Staff guidelines instruct support teams on how to handle incoming media inquiries
- [ ] No speculative claims made (e.g. naming root cause before investigation is complete)
- [ ] Output saved to `output/pr/`
