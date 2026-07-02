from database.models import SelectionProcess

from repositories.selection_process_repository import (
    create_selection_process,
    list_selection_processes as repository_list_selection_processes,
    get_selection_process_by_id,
    update_selection_process,
    delete_selection_process,
)


def create_process(
    company: str,
    title: str,
    current_status: str
):
    """
    Cria um novo processo seletivo.
    """

    if not company.strip():
        raise ValueError("Empresa é obrigatória.")

    if not title.strip():
        raise ValueError("Cargo é obrigatório.")

    process = SelectionProcess(
        company=company.strip(),
        title=title.strip(),
        current_status=current_status
    )

    return create_selection_process(process)


def list_selection_processes():
    """
    Lista todos os processos cadastrados.
    """

    return repository_list_selection_processes()


def get_process(process_id: int):
    """
    Busca um processo pelo ID.
    """

    return get_selection_process_by_id(process_id)


def update_process(
    process_id: int,
    company: str,
    title: str,
    current_status: str
):
    """
    Atualiza um processo existente.
    """

    if not company.strip():
        raise ValueError("Empresa é obrigatória.")

    if not title.strip():
        raise ValueError("Cargo é obrigatório.")

    process = SelectionProcess(
        id=process_id,
        company=company.strip(),
        title=title.strip(),
        current_status=current_status
    )

    return update_selection_process(process)


def delete_process(process_id: int):
    """
    Exclui um processo.
    """

    return delete_selection_process(process_id)