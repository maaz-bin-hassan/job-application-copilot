# Application Log Format

Maintain one Google Doc as the durable chronological application log. Append entries; never replace older entries.

Use this compact structure:

```text
## 2026-06-01 | Example Labs | React Native Developer
- job_key: 4cc9...
- status: drafted
- location: Islamabad, Pakistan
- work_mode: onsite
- source: LinkedIn
- posting_url: https://example.com/jobs/123
- application_url: https://example.com/jobs/123/apply
- contact_email: careers@example.com
- cv_used: mobile-cv.pdf
- note: Gmail draft created with mobile CV attached.
```

Supported statuses:

- `drafted`: Gmail draft created but not sent
- `sent`: application email sent after explicit approval
- `skipped_duplicate`: matching application or draft already exists
- `skipped_no_contact`: no valid direct outreach path exists
- `skipped_low_confidence`: role fit or listing details are too uncertain
- `manual_apply`: relevant role requires a website application path

Duplicate rules:

1. Check `job_key` when present.
2. Check normalized company and role.
3. Confirm with posting URL, application URL, or contact email when possible.
4. Inspect close matches manually before creating another draft.
