import streamlit as st

STATUS_OPTIONS = [
    "Candidatura enviada",
    "Triagem",
    "Entrevista RH",
    "Entrevista Técnica",
    "Teste",
    "Proposta",
    "Aprovado",
    "Reprovado",
]


def show_process_form(
    create_process,
    update_process,
    process=None,
):
    """
    Formulário reutilizável para:

    - Novo Processo
    - Editar Processo
    """

    editing = process is not None

    st.header(
        "✏️ Editar Processo"
        if editing
        else "➕ Nova candidatura"
    )

    company = process.company if editing else ""

    title = process.title if editing else ""

    status = (
        process.current_status
        if editing
        else STATUS_OPTIONS[0]
    )

    with st.form(
        "edit_process"
        if editing
        else "new_process"
    ):

        company = st.text_input(
            "Empresa",
            value=company,
        )

        title = st.text_input(
            "Cargo",
            value=title,
        )

        status = st.selectbox(
            "Status",
            STATUS_OPTIONS,
            index=STATUS_OPTIONS.index(status)
            if status in STATUS_OPTIONS
            else 0,
        )

        col1, col2 = st.columns(2)

        with col1:

            submitted = st.form_submit_button(
                "💾 Salvar"
            )

        if editing:

            with col2:

                cancel = st.form_submit_button(
                    "Cancelar"
                )

        else:

            cancel = False

        if cancel:

            st.session_state.edit_process_id = None
            st.rerun()

        if submitted:

            try:

                if editing:

                    update_process(
                        process.id,
                        company,
                        title,
                        status,
                    )

                    st.success(
                        "Processo atualizado com sucesso!"
                    )

                    st.session_state.edit_process_id = None

                else:

                    create_process(
                        company,
                        title,
                        status,
                    )

                    st.success(
                        "Processo cadastrado com sucesso!"
                    )

                st.rerun()

            except ValueError as error:

                st.error(str(error))