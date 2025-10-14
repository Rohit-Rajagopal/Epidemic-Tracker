from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.services.add_user_report_service import add_report

router = APIRouter(prefix='/user-report')


class Report(BaseModel):
    area: str
    country: str
    news: str
    url: str = ""


@router.post("/")
def add_user_report(report: Report):
    res = add_report(report.area, report.country, report.news, report.url)
    if res:
        return {"success": True, "message": "User report added successfully."}
    else:
        return {"success": False, "message": "Report not added"}