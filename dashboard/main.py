import streamlit as st

from components.process_form import show_new_process_form
from components.process_card import show_process_card

from services.selection_process_service import (
    create_process,
    list_selection_processes,
    delete_process,
)

st.set_page_config(
    page_title="Jornada New Job",
    layout="wide"
)

st.title("📋 Jornada New Job")

if "delete_process_id" not in st.session_state:
    st.session_state.delete_process_id = None

show_new_process_form(create_process)

st.divider()

processes = list_selection_processes()

st.metric(
    "Total de Processos",
    len(processes)
)

st.divider()

for process in processes:

    action = show_process_card(process)

    if action == "delete":

        st.session_state.delete_process_id = process.id

        st.rerun()

if st.session_state.delete_process_id is not None:

    st.divider()

    st.warning("⚠️ Deseja realmente excluir este processo?")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Sim, excluir"):

            delete_process(
                st.session_state.delete_process_id
            )

            st.session_state.delete_process_id = None

            st.success("Processo excluído.")

            st.rerun()

    with col2:

        if st.button("Cancelar"):

            st.session_state.delete_process_id = None

            st.rerun()