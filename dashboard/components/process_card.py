import streamlit as st


def show_process_card(process):

    with st.container(border=True):

        col1, col2, col3 = st.columns([6, 1, 1])

        with col1:
            st.subheader(process.company)
            st.write(f"**Cargo:** {process.title}")
            st.write(f"**Status:** {process.current_status}")

        with col2:

            if st.button(
                "✏️ Editar",
                key=f"edit_{process.id}"
            ):
                return "edit"

        with col3:

            if st.button(
                "🗑️ Excluir",
                key=f"delete_{process.id}"
            ):
                return "delete"

    return None