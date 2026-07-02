import streamlit as st

STATUS_OPTIONS = [
    "Candidatura enviada",
    "Triagem",
    "Entrevista RH",
    "Entrevista Técnica",
    "Teste",
    "Proposta",
    "Aprovado",
    "Reprovado"
]


def show_new_process_form(create_process):

    st.header("➕ Nova candidatura")

    with st.form("new_process"):

        company = st.text_input("Empresa")

        title = st.text_input("Cargo")

        status = st.selectbox(
            "Status",
            STATUS_OPTIONS
        )

        submitted = st.form_submit_button(
            "Salvar"
        )

        if submitted:

            try:

                create_process(
                    company,
                    title,
                    status
                )

                st.success(
                    "Processo cadastrado com sucesso!"
                )

                st.rerun()

            except ValueError as error:

                st.error(str(error))