# Job Application Copilot

An open-source [Codex](https://openai.com/codex/) skill that helps candidates
find relevant jobs, compare listings against their CV, prepare tailored Gmail
drafts, and avoid duplicate applications with a durable Google Drive log.

The workflow is deliberately review-first:

- It searches for strong matches instead of applying indiscriminately.
- It uses only experience supported by the selected CV.
- It prepares Gmail drafts when the Gmail connector is available.
- It records decisions in one chronological Google Doc when Drive is available.
- It never sends an email or submits a form without explicit user approval.

## What Is A Codex Skill?

A Codex skill is a folder containing instructions and optional helper resources
that guide Codex through a repeatable workflow. This repository is designed to
be cloned directly into the local Codex skills directory.

The main instructions live in [`SKILL.md`](SKILL.md). Supporting references and
the duplicate-key helper are loaded only when needed.

## Features

- Search current job boards, professional platforms, and employer career pages
- Filter listings by target roles, locations, work modes, recency, and experience
- Match job requirements against one or more role-specific CVs
- Select the most relevant CV for each application
- Prepare concise, customized Gmail drafts with CV-supported claims
- Keep one Google Doc as a chronological application log
- Skip roles that were already drafted or sent
- Normalize common listing URL variations with `scripts/job_key.py`
- Use the included Pakistan-focused IT profile as an optional starter example

## Safety Principles

This skill assists with careful applications. It does not automate uncontrolled
outreach.

- Codex must not invent job listings, recruiter emails, or candidate experience.
- Codex must not send an application email without explicit user approval.
- Codex must not submit website forms without explicit user approval.
- Codex must not bypass CAPTCHAs, job-board restrictions, or account protections.
- CV files, secrets, and personal contact details must stay outside this repo.

## Requirements

To use the full workflow, prepare:

1. A Codex installation that supports local skills.
2. At least one CV file available to Codex.
3. Web search or browser access for discovering current job listings.
4. A Gmail connector if you want Codex to create application drafts.
5. A Google Drive connector if you want Codex to maintain the durable log.
6. Python 3 if you want to run the optional duplicate-key helper locally.

The skill still works partially when connectors are unavailable. For example,
Codex can search jobs and write email text even when it cannot create Gmail
drafts. It should clearly report any limitation.

## Install

### Option 1: Clone With Git

Run:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/maaz-bin-hassan/job-application-copilot.git \
  ~/.codex/skills/job-application-copilot
```

### Option 2: Download A ZIP

1. Open the repository on GitHub.
2. Select **Code** and then **Download ZIP**.
3. Extract the archive.
4. Move the extracted folder to:

```text
~/.codex/skills/job-application-copilot
```

### Confirm The Installation

Check that this file exists:

```bash
test -f ~/.codex/skills/job-application-copilot/SKILL.md && \
  echo "Job Application Copilot is installed"
```

Restart Codex if the skill does not appear immediately.

## Prepare Your CV Files

Keep CV files outside this repository. Provide them to Codex through the current
workspace, attachments, or agent files supported by your environment.

You can provide one general CV or several focused versions:

```text
mobile-cv.pdf
web-cv.pdf
qa-cv.pdf
```

When multiple CVs are available, the skill asks Codex to choose the strongest
fit for each role and record which CV was used.

## Create Your Search Profile

Start from
[`references/profile-template.md`](references/profile-template.md). Define:

1. Target job titles and their priority.
2. Minimum experience requirements.
3. Preferred listing recency.
4. Allowed onsite and hybrid locations.
5. Whether international remote roles are acceptable.
6. Excluded locations or employers.
7. Preferred sources such as LinkedIn, Indeed, or employer career pages.
8. A daily Gmail draft limit.
9. Available CV labels.

You can paste the completed profile into your Codex request or keep it in a
separate personal file outside this public repository.

The bundled
[`references/example-pakistan-it-profile.md`](references/example-pakistan-it-profile.md)
is an optional starter for IT candidates searching in Pakistan. Adapt it before
use. It is not a global default.

## Connect Gmail And Google Drive

The exact connector installation flow depends on your Codex environment.

For the complete workflow:

1. Enable a Gmail connector that allows Codex to create drafts and attach files.
2. Enable a Google Drive connector that allows Codex to find, create, read, and
   update a Google Doc.
3. Ask Codex to use one Google Doc as the running application log.
4. Review the connected account before authorizing any email send.

When a connector is missing, the skill instructs Codex to continue with the
available steps and explain what could not be completed.

## Use The Skill

Invoke the skill explicitly with `$job-application-copilot`.

### Find Matching Jobs

```text
Use $job-application-copilot to find strong React Native and Flutter jobs
matching my profile. Prefer roles posted during the last 24 hours.
```

### Search And Prepare Drafts

```text
Use $job-application-copilot to find up to 5 strong matches, check my Drive
application log for duplicates, and prepare Gmail drafts with the best CV.
Do not send anything.
```

### Review A Draft

```text
Use $job-application-copilot to show me the draft for the Example Labs role
before I approve sending it.
```

### Approve A Send

```text
Send the approved Example Labs application draft. Recheck the Drive log first.
```

Approval should be specific. A request to search for jobs or create drafts is
not permission to send emails.

## How Duplicate Protection Works

The skill maintains one chronological Google Doc rather than creating a
separate document for each application. Its log format is defined in
[`references/application-log-format.md`](references/application-log-format.md).

Before creating a draft or sending an application, Codex checks:

1. The normalized company name.
2. The normalized role title.
3. The posting URL or application URL when available.
4. The hiring email when available.
5. The generated `job_key` when one was recorded.

Entries can use these statuses:

| Status | Meaning |
| --- | --- |
| `drafted` | Gmail draft created but not sent |
| `sent` | Application sent after explicit approval |
| `skipped_duplicate` | Matching role was already handled |
| `skipped_no_contact` | No valid direct outreach path exists |
| `skipped_low_confidence` | Role fit or details are too uncertain |
| `manual_apply` | Relevant role requires a website application |

## Use The Duplicate-Key Helper

The optional Python helper generates stable keys for listings:

```bash
python3 scripts/job_key.py \
  --company "Example Labs" \
  --role "React Native Developer" \
  --url "https://example.com/jobs/123?utm_source=linkedin"
```

Example output:

```text
78ca035ec14665b8c27e
```

The helper normalizes casing and spacing, removes common tracking parameters,
and strips URL fragments. As a result, common variations of the same listing
produce the same key.

## Repository Layout

```text
.
├── LICENSE
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── application-log-format.md
│   ├── example-pakistan-it-profile.md
│   └── profile-template.md
└── scripts/
    └── job_key.py
```

## Validate A Local Copy

Run the helper:

```bash
python3 scripts/job_key.py \
  --company "Example Labs" \
  --role "React Native Developer" \
  --url "https://example.com/jobs/123?utm_source=linkedin"
```

Run a Python syntax check:

```bash
python3 -m py_compile scripts/job_key.py
```

If you have the Codex `skill-creator` validation dependencies installed, run:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## Publish Your Fork On GitHub

After customizing a fork:

```bash
git add .
git commit -m "Customize job application copilot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/job-application-copilot.git
git push -u origin main
```

Do not commit private CVs, contact details, secrets, or a personal application
log.

## Contributing

Contributions are welcome. Keep the skill:

- useful for a broad range of candidates
- cautious about sending and form submission
- explicit about connector limitations
- free of personal CVs, credentials, and private application history

## License

Released under the [MIT License](LICENSE).
