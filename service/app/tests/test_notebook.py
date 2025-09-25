from pathlib import Path
import nbformat
from nbclient import NotebookClient

def test_workspace_notebook_runs_and_prints_hello():
    nb_path = Path(__file__).resolve().parents[2] / "workspace" / "main.ipynb"
    nb = nbformat.read(nb_path, as_version=4)
    client = NotebookClient(nb, timeout=60, kernel_name="python3", allow_errors=False)
    executed = client.execute()

    outputs = []
    for cell in executed.cells:
        if "outputs" in cell:
            for out in cell["outputs"]:
                if out.get("output_type") == "stream" and "text" in out:
                    outputs.append(out["text"])
                if out.get("output_type") in {"display_data", "execute_result"}:
                    data = out.get("data", {})
                    if "text/plain" in data:
                        outputs.append(data["text/plain"])

    text = "".join(outputs)
    assert "Hello Jupyter" in text
