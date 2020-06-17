from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden, JsonResponse, HttpResponseNotAllowed
from siteapp.models import Project, User, Organization
from django.urls import reverse

import json, re, os


import logging
logging.basicConfig()
import structlog
from structlog import get_logger
from structlog.stdlib import LoggerFactory
structlog.configure(logger_factory=LoggerFactory())
structlog.configure(processors=[structlog.processors.JSONRenderer()])
logger = get_logger()
# logger = logging.getLogger(__name__)

def test(request):
    # Simple test page of routing for controls
    output = "Test works."
    html = "<html><body><p>{}</p></body></html>".format(output)
    return HttpResponse(html)

# Create your views here.

def about(request):
    # Simple test page of routing for controls
    # version
    # copyright
    # license
    # github
    # vendor
    output = """
About
=====

GovReady-Q

version {version}
commit {commit}

(c) 2020 GovReady PBC

""".format(version=settings.APP_VERSION_STRING, commit=settings.APP_VERSION_COMMIT)

    html = "<html><body><pre>{}</pre></body></html>".format(output)
    return HttpResponse(html)

def changelog(request):
    """Display CHANGELOG.md"""

    import pathlib
    base_dir = pathlib.Path(__file__).parent.parent
    print(base_dir)
    changelog_path = os.path.join(base_dir, 'CHANGELOG.md')
    if not os.path.exists(changelog_path):
        output = "No CHANGELOG.md"
    else:
        with open(changelog_path) as fd:
            output = fd.read()

    html = "<html><body><pre>{}</pre></body></html>".format(output)
    return HttpResponse(html)
