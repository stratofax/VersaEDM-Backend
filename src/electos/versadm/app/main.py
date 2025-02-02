from fastapi import FastAPI

from versadm.app.db.in_memory import InMemoryDb
from versadm.app import routers


def create_app(app_state=InMemoryDb()) -> FastAPI:
    app = FastAPI()

    app.include_router(routers.candidate.create_router(app_state))
    app.include_router(routers.contest.create_router(app_state))
    app.include_router(routers.election.create_router(app_state))
    app.include_router(routers.election_report.create_router(app_state))
    app.include_router(routers.health.router)
    app.include_router(routers.office.create_router(app_state))
    app.include_router(routers.party.create_router(app_state))
    app.include_router(routers.person.create_router(app_state))
    app.include_router(routers.reporting_unit.create_router(app_state))

    return app
