# 🛠️ Troubleshooting

Find your error below. **Tip:** the most useful line of a Python error is usually the **last one**.

---

## Python and the virtual environment

| Problem | Fix |
|---|---|
| `python` is not recognized | Python isn't on your PATH. Reinstall Python from python.org and tick **"Add python.exe to PATH"**, or try `py` instead of `python`. |
| `running scripts is disabled on this system` (activating `.venv`) | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, answer `Y`, then `.venv\Scripts\Activate.ps1` again. |
| Prompt doesn't start with `(.venv)` | Activate it: `.venv\Scripts\Activate.ps1` (Windows) or `source .venv/bin/activate` (macOS). |
| `pip install` fails with a network error | Check your internet connection, then retry. Slow connection? Add `--timeout 120`. |
| `ModuleNotFoundError: No module named 'pandas'` (or seaborn, sklearn…) | Either the environment isn't active, or the notebook is using the wrong kernel. Activate `.venv`, run `pip install -r requirements.txt`, then pick the **.venv** kernel in the notebook (top-right). |
| `ModuleNotFoundError: No module named 'src'` | Run the **first code cell** of the notebook (Part 0.1) again. It tells Python where `src/` is. For the app: run `streamlit run app/streamlit_app.py` **from the project folder**, not from inside `app/`. |

## The notebook

| Problem | Fix |
|---|---|
| `NameError: name '____' is not defined` | You still have a blank `____` (four underscores) to fill in, in that cell. |
| `NameError: name 'df' is not defined` (or `df_raw`, `ols`, `X_train`…) | That variable is created in an earlier cell you haven't run. Click **Run All**, or run the cells above in order. Restarting VS Code clears all variables. |
| ❌ in a check cell | Read the 💡 tip under it, fix the TODO cell above, **run the TODO cell again, then the check cell**. |
| `KeyError: 'some_column'` | The column name is misspelled. Copy it exactly from `df.columns`. Names are case-sensitive. |
| `SyntaxError` | Usually a missing bracket `)`, quote `"` or comma. Look at the line the arrow `^` points to and the line before it. |
| `IndentationError` | Python uses spaces for structure. Line the code up with the lines around it (use the Tab key consistently). |
| `FileNotFoundError: ...nasarawa_yam_survey_synthetic.csv` | You opened a different folder in VS Code. Open the **project folder** (the one containing `README.md`). |
| The kernel keeps dying / very slow | Close other programs. Restart the kernel. Part 6 takes 1–2 minutes, which is normal. |
| Can't choose `.venv` as the kernel | `pip install ipykernel` inside the active environment, then reload VS Code (**Ctrl + Shift + P → Developer: Reload Window**). |
| Hint/answer boxes don't open | Click on the ▶ **Hint** text itself. If your VS Code shows raw HTML, view the notebook on GitHub instead, where the boxes work. |

## Git and GitHub

| Problem | Fix |
|---|---|
| `Author identity unknown` / `Please tell me who you are` | `git config --global user.name "Your Name"` and `git config --global user.email "your-github-email"` |
| My commits don't show my GitHub picture / don't count as mine | Your Git email doesn't match your GitHub email. Fix it with the command above (future commits will count), or add that email in GitHub → **Settings → Emails**. |
| `Permission denied` / `403` when pushing | You haven't **accepted the collaborator invitation** (check https://github.com/notifications), or you cloned someone else's copy. Ask your coordinator. |
| `Repository not found` | Check the link. If the repo is private, you must be a collaborator *and* signed in. |
| `rejected ... fetch first` | Someone pushed before you: `git pull` then `git push`. |
| `Your local changes would be overwritten by merge` | See [TEAM_WORKFLOW.md → When things go wrong](TEAM_WORKFLOW.md#when-things-go-wrong). |
| `CONFLICT ... group_project.ipynb` | `git merge --abort`, then see [TEAM_WORKFLOW.md](TEAM_WORKFLOW.md#conflict-content-merge-conflict-in-notebooksgroup_projectipynb). |
| An editor full of `~` symbols opened after `git pull` | It's Vim asking for a merge message. Type `:wq` and press Enter. |
| Sign-in window never appears on push | Run `git config --global credential.helper manager` (Windows), then push again. |
| Invitation expired | Coordinator: Settings → Collaborators → remove the person → invite again. |

## Streamlit

| Problem | Fix |
|---|---|
| `streamlit` is not recognized | Activate `.venv` first. Or run `python -m streamlit run app/streamlit_app.py`. |
| The app says *No trained model or clean data found yet* | Part 6 hasn't been pushed. ML lead: run Part 6 and push. Everyone else: `git pull`. |
| My change doesn't appear | Did you **save** the file? Then click **Rerun** in the browser (or press **R**). |
| Red error box in the app | Read the **last line**; it shows the file and line number. Usually a typo in the TODO you just did. Undo it (**Ctrl + Z**), save, rerun, and try again carefully. |
| `Port 8501 is already in use` | An old app is still running. Press **Ctrl + C** in the old terminal, or run with `--server.port 8502`. |
| Deployment on Streamlit Cloud fails | Check that `requirements.txt` and the files in `models/` and `data/processed/` are pushed to GitHub, and the main file path is `app/streamlit_app.py`. |

---

Still stuck? Post in the workshop WhatsApp group with **(1)** what you were doing, **(2)** a screenshot of the **whole** error, **(3)** what you've tried.
