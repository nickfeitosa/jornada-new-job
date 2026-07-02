import streamlit as st

from services.selection_process_service import (
    create_process,
    list_selection_processes
)

st.set_page_config(
    page_title="Jornada New Job",
    layout="wide"
)

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

        except ValueError as error:

            st.error(str(error))

st.divider()

processes = list_selection_processes()

st.metric(
    "Total de Processos",
    len(processes)
)

st.divider()

for process in processes:

    st.subheader(process.company)

    st.write(f"Cargo: {process.title}")

    st.write(f"Status: {process.current_status}")

    st.divider()