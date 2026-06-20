from database.base import SessionLocal
from database.models import SelectionProcess


def create_selection_process(
    company: str,
    title: str,
    status: str
):
    session = SessionLocal()

    try:

        process = SelectionProcess(
            company=company,
            title=title,
            current_status=status
        )

        session.add(process)

        session.commit()

        return process

    finally:
        session.close()


def list_selection_processes():

    session = SessionLocal()

    try:

        return session.query(
            SelectionProcess
        ).all()

    finally:
        session.close()