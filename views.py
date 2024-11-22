from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from lnbits.core.models import User
from lnbits.decorators import check_user_exists
from lnbits.helpers import template_renderer

fluttr_generic_router = APIRouter()


def fluttr_renderer():
    return template_renderer(["fluttr/templates"])


#######################################
##### ADD YOUR PAGE ENDPOINTS HERE ####
#######################################


# Backend admin page


@fluttr_generic_router.get("/", response_class=HTMLResponse)
async def index(req: Request, user: User = Depends(check_user_exists)):
    return fluttr_renderer().TemplateResponse(
        "fluttr/index.html", {"request": req, "user": user.json()}
    )
