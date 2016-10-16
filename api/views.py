#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.conf import settings
import requests
import json

def index(request):
	keyword = request.GET.get("q") or 'import error'
	url = "https://api.stackexchange.com/2.2/similar?order=desc&sort=activity&title=%s&site=stackoverflow&key=XvJTrWoA7KBmRZLAsX8ERQ(("%(keyword)
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	return JsonResponse(data)
