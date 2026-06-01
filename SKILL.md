---
name: job-application-copilot
description: Find relevant jobs, rank strong matches against a candidate profile and CV, prevent duplicate applications with a durable Google Drive log, and prepare tailored Gmail drafts. Use when Codex needs to search for jobs, shortlist roles, draft application emails, create Gmail drafts, track application decisions in one Google Doc, or avoid applying to the same role twice.
---

# Job Application Copilot

## Overview

Run a careful job-search and application-drafting workflow. Favor a small number of strong matches, use only CV-supported claims, record every decision in one durable Google Drive log, and never send email without explicit user approval.

## Start

1. Read the user's current request, available candidate profile, and CV files.
2. Ask for a CV before tailoring applications when no relevant CV is available.
3. Use the user's profile when provided. If the user wants a starter profile, adapt [profile-template.md](references/profile-template.md). For Pakistan-focused IT searches, optionally adapt [example-pakistan-it-profile.md](references/example-pakistan-it-profile.md).
4. Discover available web-search, browser, Gmail, and Google Drive tools. Use connector tools when available. If a required connector is unavailable, continue with the parts that are possible and state the limitation.
5. Open or locate one existing Google Doc application log before creating drafts. Create one only if no log exists and Drive access is available. Follow [application-log-format.md](references/application-log-format.md).

## Search And Filter

1. Search current job sources requested by the user. Include major job boards, employer career pages, and professional platforms when available.
2. Respect profile rules for role type, location, work mode, recency, experience, exclusions, and daily draft limit.
3. Treat missing details as unknown. Do not invent a location, work mode, experience requirement, recruiter email, or application URL.
4. Skip jobs that clearly violate the profile. Keep uncertain roles separate from strong matches.
5. Prefer high-quality matches over filling a quota.

## Match Against CV

1. Select the most relevant CV for each role. When multiple CVs exist, choose by role type and record the selected file label.
2. Use only skills, tools, projects, experience, certifications, and achievements supported by the selected CV or explicitly provided by the user.
3. Rank jobs by fit and prioritize roles where the candidate's actual evidence addresses the listing requirements.
4. Keep the rationale concise and factual.

## Prevent Duplicates

1. Read the Google Doc log before preparing outreach.
2. Treat a role as already handled when company and role clearly match and at least one stable identifier also matches, such as posting URL, application URL, hiring email, or generated `job_key`.
3. Also inspect close company-and-role matches manually because job-board URLs can vary.
4. Use `scripts/job_key.py` when a stable normalized key helps:

```bash
python3 scripts/job_key.py \
  --company "Example Labs" \
  --role "React Native Developer" \
  --url "https://example.com/jobs/123"
```

5. Skip creating a second draft for an existing `drafted` or `sent` record unless the user explicitly asks to replace or revise it.
6. Append a `skipped_duplicate` entry when a duplicate is encountered.

## Prepare Drafts

1. Draft a concise, natural application email for each strong, non-duplicate role with a valid direct email path.
2. Mention the exact role and company. Connect CV-supported evidence to the listing without exaggeration.
3. Vary wording across drafts so the messages are genuinely tailored.
4. Attach the selected CV when Gmail tools support attachments.
5. Create a Gmail draft when Gmail access is available. Do not send it.
6. Append a `drafted` entry to the Google Doc log immediately after draft creation.
7. For jobs without a valid direct email path, record `skipped_no_contact` and return the application link or best available path.

## Send Only With Approval

1. Send a prepared application only after the user explicitly approves sending it in the current conversation.
2. Recheck the Drive log immediately before sending.
3. Update the existing draft record or append a `sent` entry after a successful send.
4. Never claim an email was drafted, attached, logged, or sent unless the corresponding tool action succeeded.

## Report

Return a concise execution summary with:

- jobs drafted and the CV used
- jobs sent only when explicitly approved
- duplicates skipped
- jobs skipped with reasons
- relevant roles requiring manual application through a link
- connector limitations or details that could not be verified

Include full email text only when the user asks to review it or when Gmail draft creation is unavailable.

## Boundaries

- Do not fabricate listings, details, contacts, candidate claims, or tool results.
- Do not bypass job-board restrictions, CAPTCHAs, or account protections.
- Do not submit website forms or send emails without explicit user approval.
- Do not store CV contents, secrets, or personal contact details inside this reusable skill folder.
- Do not overwrite older Drive log entries. Keep the log chronological.
