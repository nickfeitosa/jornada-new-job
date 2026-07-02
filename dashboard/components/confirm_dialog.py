import streamlit as st


def show_delete_confirmation(process):

    st.warning(
        f"Deseja realmente excluir o processo da empresa **{process.company}**?"
    )

    col1, col2 = st.columns(2)

    with col1:

        confirm = st.button(
            "✅ Sim"
        )

    with col2:

        cancel = st.button(
            "❌ Cancelar"
        )

    return confirm, cancel