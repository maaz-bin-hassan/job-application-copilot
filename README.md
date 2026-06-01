# Job Application Copilot

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Codex Plugin](https://img.shields.io/badge/Codex-plugin-2563EB)](https://developers.openai.com/codex/plugins)

An open-source Codex plugin for finding relevant jobs, comparing listings
against a CV, preparing tailored Gmail drafts, and preventing duplicate
applications with a durable Google Drive log.

The workflow is deliberately review-first:

- Search for strong matches instead of applying indiscriminately.
- Use only experience supported by the selected CV.
- Prepare Gmail drafts when Gmail tools are available.
- Record decisions in one chronological Google Doc when Drive tools are available.
- Never send an email or submit a form without explicit user approval.

## Why Use It?

Job searching becomes repetitive quickly. This plugin gives Codex a reusable
process for searching, matching, drafting, and tracking applications without
sacrificing accuracy or user control.

It works well for:

- developers and QA engineers looking for relevant roles
- candidates with separate mobile, web, and QA CVs
- people who want polished application drafts without duplicate outreach
- anyone who wants one searchable log of drafted, sent, and skipped roles

## Features

- Search current job boards, professional platforms, and employer career pages
- Filter by target role, location, work mode, recency, and experience
- Match job requirements against one or more role-specific CVs
- Select the strongest CV for each application
- Prepare concise Gmail drafts using CV-supported claims
- Keep one Google Doc as a chronological application log
- Skip roles that were already drafted or sent
- Normalize common listing URL variations with `scripts/job_key.py`
- Start quickly with an optional Pakistan-focused IT example profile

## Safety Principles

This plugin helps candidates apply carefully. It does not automate uncontrolled
outreach.

- Do not invent job listings, recruiter emails, or candidate experience.
- Do not send an application email without explicit user approval.
- Do not submit website forms without explicit user approval.
- Do not bypass CAPTCHAs, job-board restrictions, or account protections.
- Keep CV files, secrets, and personal contact details outside this repository.

## Requirements

To use the complete workflow, prepare:

1. A current Codex CLI or Codex app installation with plugin support.
2. At least one CV file available to Codex.
3. Web search or browser access for current job discovery.
4. Gmail tools if you want Codex to create application drafts.
5. Google Drive tools if you want Codex to maintain the durable log.
6. Python 3 if you want to run the optional duplicate-key helper locally.

The bundled plugin teaches the workflow. Gmail and Google Drive remain separate
connected tools so users stay in control of their own accounts and permissions.

The plugin still works partially when a connector is unavailable. For example,
Codex can search roles and write email text even when it cannot create a Gmail
draft. It should report the limitation clearly.

## Install As A Codex Plugin

Codex plugins can be distributed through marketplace repositories. This
repository includes a marketplace catalog and one installable plugin.

### 1. Add The Marketplace

Run:

```bash
codex plugin marketplace add maaz-bin-hassan/job-application-copilot
```

### 2. Install From The CLI

Run:

```bash
codex plugin add job-application-copilot@job-application-copilot
```

Start a new Codex thread after installation.

### 3. Or Install From The Plugin Directory

Start Codex:

```bash
codex
```

Then enter:

```text
/plugins
```

1. Open the **Job Application Copilot** marketplace tab.
2. Select **Job Application Copilot**.
3. Choose **Install plugin**.
4. Start a new Codex thread after installation.

In the Codex app, open **Plugins**, select the marketplace, and choose
**Add to Codex**.

### 4. Invoke The Plugin

Use the plugin directly:

```text
@job-application-copilot Find strong matching jobs and prepare Gmail drafts.
Do not send anything.
```

You can also invoke the bundled skill explicitly:

```text
$job-application-copilot Find strong matching jobs and prepare Gmail drafts.
Do not send anything.
```

## Install Only The Skill

If your Codex version supports skills but not plugins yet, install the bundled
skill directly:

```text
$skill-installer install https://github.com/maaz-bin-hassan/job-application-copilot/tree/main/plugins/job-application-copilot/skills/job-application-copilot
```

Restart Codex after installation.

## Prepare Your CV Files

Keep CV files outside this repository. Provide them to Codex through your
workspace, attachments, or agent files supported by your environment.

You can provide one general CV or several focused versions:

```text
mobile-cv.pdf
web-cv.pdf
qa-cv.pdf
```

When multiple CVs are available, the skill asks Codex to select the strongest
fit for each role and record which CV was used.

## Create Your Search Profile

Start from
[`profile-template.md`](plugins/job-application-copilot/skills/job-application-copilot/references/profile-template.md).
Define:

1. Target job titles and their priority.
2. Minimum experience requirements.
3. Preferred listing recency.
4. Allowed onsite and hybrid locations.
5. Whether international remote roles are acceptable.
6. Excluded locations or employers.
7. Preferred sources such as LinkedIn, Indeed, or employer career pages.
8. A daily Gmail draft limit.
9. Available CV labels.

Paste the completed profile into your Codex request or keep it in a separate
private file outside this public repository.

The bundled
[`example-pakistan-it-profile.md`](plugins/job-application-copilot/skills/job-application-copilot/references/example-pakistan-it-profile.md)
is an optional starter for IT candidates searching in Pakistan. Adapt it before
use. It is not a global default.

## Connect Gmail And Google Drive

For the complete workflow:

1. Enable Gmail tools that allow Codex to create drafts and attach files.
2. Enable Google Drive tools that allow Codex to find, create, read, and update
   a Google Doc.
3. Ask Codex to use one Google Doc as the running application log.
4. Review the connected account before authorizing any email send.

When a connector is missing, the plugin instructs Codex to continue with the
available steps and explain what could not be completed.

## Example Prompts

### Find Matching Jobs

```text
@job-application-copilot Find strong React Native and Flutter jobs matching my
profile. Prefer roles posted during the last 24 hours.
```

### Search And Prepare Drafts

```text
@job-application-copilot Find up to 5 strong matches, check my Drive application
log for duplicates, and prepare Gmail drafts with the best CV. Do not send anything.
```

### Review A Draft

```text
@job-application-copilot Show me the draft for the Example Labs role before I
approve sending it.
```

### Approve A Send

```text
Send the approved Example Labs application draft. Recheck the Drive log first.
```

Approval should be specific. A request to search for jobs or create drafts is
not permission to send emails.

## How Duplicate Protection Works

The plugin maintains one chronological Google Doc instead of creating a
separate document for each application. Its log format is defined in
[`application-log-format.md`](plugins/job-application-copilot/skills/job-application-copilot/references/application-log-format.md).

Before creating a draft or sending an application, Codex checks:

1. The normalized company name.
2. The normalized role title.
3. The posting URL or application URL when available.
4. The hiring email when available.
5. The generated `job_key` when one was recorded.

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
python3 plugins/job-application-copilot/skills/job-application-copilot/scripts/job_key.py \
  --company "Example Labs" \
  --role "React Native Developer" \
  --url "https://example.com/jobs/123?utm_source=linkedin"
```

Example output:

```text
78ca035ec14665b8c27e
```

The helper normalizes casing and spacing, removes common tracking parameters,
and strips URL fragments. Common variations of the same listing produce the
same key.

## Repository Layout

```text
.
├── .agents/plugins/marketplace.json
├── LICENSE
├── README.md
└── plugins/
    └── job-application-copilot/
        ├── .codex-plugin/plugin.json
        └── skills/
            └── job-application-copilot/
                ├── SKILL.md
                ├── agents/openai.yaml
                ├── references/
                └── scripts/job_key.py
```

## Validate A Local Copy

Run the helper:

```bash
python3 plugins/job-application-copilot/skills/job-application-copilot/scripts/job_key.py \
  --company "Example Labs" \
  --role "React Native Developer" \
  --url "https://example.com/jobs/123?utm_source=linkedin"
```

Run a Python syntax check:

```bash
python3 -m py_compile \
  plugins/job-application-copilot/skills/job-application-copilot/scripts/job_key.py
```

## Publish Your Fork

After customizing a fork:

```bash
git add .
git commit -m "Customize job application copilot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/job-application-copilot.git
git push -u origin main
```

Users of your fork can then add your marketplace:

```bash
codex plugin marketplace add YOUR_USERNAME/job-application-copilot
```

Do not commit private CVs, personal contact details, secrets, or an application
log.

## Official Codex Plugin Directory

OpenAI's documentation currently says that adding plugins to the official
Plugin Directory and self-serve plugin publishing are coming soon.

Until that opens, distribute this plugin through its GitHub marketplace command,
share it with the Codex community, and collect feedback from real users.

## Help The Project Grow

- Star the repository if the plugin saves you time.
- Share a short demo showing job discovery, duplicate detection, and Gmail drafts.
- Open issues for missing workflows or unclear setup steps.
- Submit focused pull requests that keep candidate data private.

## Contributing

Contributions are welcome. Keep the plugin:

- useful for a broad range of candidates
- cautious about sending and form submission
- explicit about connector limitations
- free of personal CVs, credentials, and private application history

## License

Released under the [MIT License](LICENSE).
