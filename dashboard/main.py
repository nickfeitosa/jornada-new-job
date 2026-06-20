import os
import sys

import streamlit as st

# Adiciona a raiz do projeto ao PATH
PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from services.selection_process_service import (
    list_selection_processes
)

st.set_page_config(
    page_title="Jornada New Job",
    layout="wide"
)

st.title("📋 Jornada New Job")

processes = list_selection_processes()

st.metric(
    "Total de Processos",
    len(processes)
)

st.divider()

for process in processes:

    st.subheader(
        process.company
    )

    st.write(
        f"Cargo: {process.title}"
    )

    st.write(
        f"Status: {process.current_status}"
    )

    st.divider()