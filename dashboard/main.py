import streamlit as st

from services.selection_process_service import (
    create_process,
    list_selection_processes,
    delete_process
)

st.set_page_config(
    page_title="Jornada New Job",
    layout="wide"
)


# ==========================
# FORMULÁRIO DE CADASTRO
# ==========================
if "editing_process" not in st.session_state:
    st.session_state.editing_process = None

st.title("📋 Jornada New Job")

st.header("Nova candidatura")

with st.form("new_process"):

    company = st.text_input("Empresa")

    title = st.text_input("Cargo")

    status = st.selectbox(
        "Status",
        [
            "Candidatura enviada",
            "Triagem",
            "Entrevista RH",
            "Entrevista Técnica",
            "Teste",
            "Proposta",
            "Aprovado",
            "Reprovado"
        ]
    )

    submitted = st.form_submit_button("Salvar")

    if submitted:

        try:

            create_process(
                company,
                title,
                status
            )

            st.success("Processo cadastrado com sucesso!")

            st.rerun()

        except ValueError as error:

            st.error(str(error))

st.divider()

processes = list_selection_processes()

st.metric(
    "Total de Processos",
    len(processes)
)

st.divider()

# ==========================
# LISTAGEM
# ==========================

for process in processes:

    col1, col2 = st.columns([5, 1])

    with col1:

        st.subheader(process.company)

        st.write(f"**Cargo:** {process.title}")

        st.write(f"**Status:** {process.current_status}")

    with col2:

        if st.button(
            "🗑️ Excluir",
            key=f"delete_{process.id}"
        ):

            delete_process(process.id)

            st.success("Processo excluído!")

            st.rerun()

    st.divider()