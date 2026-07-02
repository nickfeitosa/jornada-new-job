from database.base import SessionLocal
from database.models import SelectionProcess


def create_selection_process(process: SelectionProcess):
    """
    Salva um processo seletivo no banco.
    """

    with SessionLocal() as session:
        session.add(process)
        session.commit()
        session.refresh(process)

    return process


def list_selection_processes():
    """
    Retorna todos os processos cadastrados.
    """

    with SessionLocal() as session:
        return (
            session.query(SelectionProcess)
            .order_by(SelectionProcess.id)
            .all()
        )


def get_selection_process_by_id(process_id: int):
    """
    Busca um processo pelo ID.
    """

    with SessionLocal() as session:
        return (
            session.query(SelectionProcess)
            .filter(SelectionProcess.id == process_id)
            .first()
        )


def update_selection_process(process: SelectionProcess):
    """
    Atualiza um processo existente.
    """

    with SessionLocal() as session:

        existing = session.get(
            SelectionProcess,
            process.id
        )

        if existing is None:
            return None

        existing.company = process.company
        existing.title = process.title
        existing.current_status = process.current_status

        session.commit()
        session.refresh(existing)

        return existing


def delete_selection_process(process_id: int):
    """
    Remove um processo do banco.
    """

    with SessionLocal() as session:

        process = session.get(
            SelectionProcess,
            process_id
        )

        if process is None:
            return False

        session.delete(process)
        session.commit()

        return True