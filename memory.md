# Learnalytics — Session Memory

## Project Overview
Django 6.0.3 web app for student performance analytics. Postgres in production (Supabase), SQLite for local dev. Plain CSS (no Tailwind). Separate Admin (Django) and Teacher (custom) login flows.

---

## Session: CSS Theme Refactor + Admin-Login Fix + Seed Data (v0.2 Branch)

### Changes Made

#### 1. CSS Theme Variables (`static/css/variables.css`)
- Created `static/css/variables.css` with `:root` (light mode) and `.dark` blocks for shared custom properties.
- Added `<link rel="stylesheet" href="{% static 'css/variables.css' %}">` **before** each template's existing CSS link in all 16 templates.
- Added `class="dark"` to `<html>` tag in all 16 templates.
- **Key constraint:** Kept all old `:root` blocks and cyan color values intact; only *added* the new variables. No existing styles were changed.

#### 2. Admin-Login Redirect Fix
- **Problem:** Django admin login auto-logs in a user already authenticated (e.g., a Teacher), bypassing credential prompt.
- **Solution:** Created `admin_login_view` in `teacher/views.py` that calls `logout(request)` then redirects to `/admin/login/`.
- Added `/admin-login/` route in `learnalytics/urls.py` pointing to this view.
- Updated Admin link in `templates/home.html` from `{% url 'admin:login' %}` to `{% url 'admin_login' %}`.
- **Result:** Teacher → Admin flow now always shows fresh login form.

#### 3. Database: SQLite → Postgres
- Temporarily switched `DATABASES` to SQLite for local testing of seed data.
- Reverted back to Supabase Postgres config (via env vars) when user said "end".
- **Note:** PostgreSQL is not running locally — `psycopg2.OperationalError` expected.

#### 4. Seed Data Command (`students/management/commands/seed_data.py`)
- Idempotent — skips records that already exist.
- Seeds: 1 admin (`admin`/`admin123`), 1 teacher (`teacher`/`teacher123`), 10 students, 40 marks, 3 feedback entries.
- **Known limitation:** `Mark.exam_date` has `auto_now_add=True`, so explicit dates are ignored on creation.

#### 5. Branching
- Branch `v0.2` created from `main` after `git reset --soft HEAD~1` (which undid the previous commit but kept changes staged).
- All changes committed as `43da6bf` on `v0.2`.
- Pushed to GitHub as `origin/v0.2`.

### Rollbacks / Reversions
- CSS theme refactoring (old `:root`/cyan removal) was reverted by user — only the additive `variables.css` + `class="dark"` approach was kept.
- SQLite revert to Postgres was done on user request.

### Accidental Deletions
- `git clean -fd` removed untracked files: `templates/students/dashboard.html` (never restored), migration files, AI model files (`students/ai/*.pkl`).

### Design Decisions
- **No framework upgrades** — plain CSS, Django admin + custom teacher views.
- **Teacher → Admin re-login** is explicit (not automatic) to enforce separation.
- **Seed data is idempotent** — safe to run multiple times.

### Open Issues / Next Steps
- `templates/students/dashboard.html` may still be missing if needed.
- PostgreSQL must be running or env vars configured before running server.
- For local dev without Postgres: switch `DATABASES` back to SQLite.
- GitHub push requires user's manual credential/SSH setup.
