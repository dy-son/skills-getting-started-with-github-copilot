## Plan: Add FastAPI backend tests

TL;DR: Add a new `tests/` directory with pytest-based FastAPI tests for the backend endpoints in `src/app.py`, then validate using `pytest`.

**Steps**
1. Create a new directory `tests/` at the repository root.
2. Add a test module `tests/test_app.py`.
   - Import `TestClient` from `fastapi.testclient`.
   - Import the FastAPI app from `src.app`.
   - Create a client instance.
3. Write tests covering the backend behavior:
   - `test_get_activities_returns_activities`: GET `/activities` returns all activity data.
   - `test_signup_for_activity_returns_success`: POST signup adds a participant and returns a success message.
   - `test_signup_duplicate_participant_returns_400`: duplicate signup returns HTTP 400.
   - `test_remove_participant_returns_success`: DELETE removes a participant and updates the activity.
   - `test_remove_nonexistent_participant_returns_404`: deleting a missing participant returns HTTP 404.
4. Ensure the `tests` directory is separate from `src/` and does not require app code changes.
5. Run `pytest` from the repo root to verify the new tests.

**Relevant files**
- `src/app.py` — backend endpoints to test
- `pytest.ini` — existing pytest configuration
- `requirements.txt` — verify test dependencies like `pytest` if needed

**Verification**
1. `pytest` should discover `tests/test_app.py` and run all tests.
2. Confirm the activity data and participant changes behave as expected.
3. If `pytest` is not installed, add it to the project dependencies.

**Decision**
- Use `TestClient` for backend tests instead of browser-based UI tests, keeping the focus on FastAPI behavior.
