import streamlit as st

from components.process_form import show_process_form
from components.process_card import show_process_card

from services.selection_process_service import (
    create_process,
    list_selection_processes,
    get_process,
    update_process,
    delete_process,
)

st.set_page_config(
    page_title="Jornada New Job",
    layout="wide",
)

st.title("📋 Jornada New Job")

# ===========================
# Session State
# ===========================

if "delete_process_id" not in st.session_state:
    st.session_state.delete_process_id = None

if "edit_process_id" not in st.session_state:
    st.session_state.edit_process_id = None

# ===========================
# Formulário
# ===========================

if st.session_state.edit_process_id is not None:

    process = get_process(
        st.session_state.edit_process_id
    )

    show_process_form(
        create_process=create_process,
        update_process=update_process,
        process=process,
    )

else:

    show_process_form(
        create_process=create_process,
        update_process=update_process,
    )

st.divider()

# ===========================
# Lista
# ===========================

processes = list_selection_processes()

st.metric(
    "Total de Processos",
    len(processes),
)

st.divider()

for process in processes:

    action = show_process_card(process)

    if action == "edit":

        st.session_state.edit_process_id = process.id

        st.rerun()

    if action == "delete":

        st.session_state.delete_process_id = process.id

        st.rerun()

# ===========================
# Exclusão
# ===========================

if st.session_state.delete_process_id is not None:

    st.divider()

    st.warning(
        "⚠️ Deseja realmente excluir este processo?"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Sim, excluir"):

            delete_process(
                st.session_state.delete_process_id
            )

            st.session_state.delete_process_id = None

            st.success(
                "Processo excluído com sucesso!"
            )

            st.rerun()

    with col2:

        if st.button("Cancelar"):

            st.session_state.delete_process_id = None

            st.rerun()