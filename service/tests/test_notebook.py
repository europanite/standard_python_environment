import os

import nbformat
from nbclient import NotebookClient


def test_workspace_notebook_runs_and_prints_hello():
    nb_path = os.path.join("/app", "main.ipynb")
    assert nb_path.exists(), f"Notebook not found: {nb_path}"

    nb = nbformat.read(str(nb_path), as_version=4)

    client = NotebookClient(
        nb,
        timeout=120,
        kernel_name="python3",
        allow_errors=False,
        record_timing=False,
    )
    client.execute()

    outs = []
    for cell in nb.cells:
        if "outputs" in cell:
            for out in cell["outputs"]:
                if out.get("output_type") in ("stream", "execute_result"):
                    text = ""
                    if out.get("text"):
                        text = out["text"]
                    elif "data" in out and "text/plain" in out["data"]:
                        text = out["data"]["text/plain"]
                    outs.append(text or "")
    joined = "\n".join(outs)
    assert "hello" in joined.lower()
